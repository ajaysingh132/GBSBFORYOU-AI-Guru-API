import logging
import os

import httpx

logger = logging.getLogger(__name__)


def supabase_configured() -> bool:
    return bool(
        os.getenv("SUPABASE_URL", "").strip()
        and (
            os.getenv("SUPABASE_SECRET_KEY", "").strip()
            or os.getenv("SUPABASE_SERVICE_ROLE_KEY", "").strip()
        )
    )


def save_interaction(decision) -> bool:
    """Save minimal workflow metadata; never store the full question or student answer."""
    base_url = os.getenv("SUPABASE_URL", "").strip().rstrip("/")
    secret_key = (
        os.getenv("SUPABASE_SECRET_KEY", "").strip()
        or os.getenv("SUPABASE_SERVICE_ROLE_KEY", "").strip()
    )
    if not base_url or not secret_key:
        return False

    payload = {
        "mode": decision.mode,
        "class_level": decision.class_level,
        "subject_code": decision.subject_code,
        "curriculum_session": decision.session,
        "concept": decision.concept[:120],
    }
    try:
        response = httpx.post(
            f"{base_url}/rest/v1/ai_guru_interactions",
            headers={
                "apikey": secret_key,
                "Authorization": f"Bearer {secret_key}",
                "Content-Type": "application/json",
                "Prefer": "return=minimal",
            },
            json=payload,
            timeout=5.0,
        )
        response.raise_for_status()
        return True
    except (httpx.HTTPError, ValueError) as exc:
        logger.warning("Supabase interaction write failed: %s", type(exc).__name__)
        return False
