import logging
import os

import httpx

logger = logging.getLogger(__name__)


def supabase_key_format_valid(secret_key: str) -> bool:
    """Accept Supabase modern secret keys or legacy service_role JWTs only."""
    key = secret_key.strip()
    return key.startswith("sb_secret_") or key.startswith("eyJ")


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
    if not supabase_key_format_valid(secret_key):
        logger.error(
            "Supabase write disabled: SUPABASE_SECRET_KEY has an unsupported format; "
            "expected sb_secret_* or a legacy service_role JWT (eyJ...)."
        )
        return False

    payload = {
        "mode": decision.mode,
        "class_level": decision.class_level,
        "subject_code": decision.subject_code,
        "curriculum_session": decision.session,
        "concept": decision.concept[:120],
    }
    try:
        headers = {
            "apikey": secret_key,
            "Content-Type": "application/json",
            "Prefer": "return=minimal",
        }
        # Modern sb_secret_* keys are API keys, not JWTs; sending them as
        # Bearer tokens causes Supabase authentication failures. Keep the
        # Authorization header only for legacy JWT-based service_role keys.
        if secret_key.startswith("eyJ"):
            headers["Authorization"] = f"Bearer {secret_key}"

        response = httpx.post(
            f"{base_url}/rest/v1/ai_guru_interactions",
            headers=headers,
            json=payload,
            timeout=5.0,
        )
        response.raise_for_status()
        return True
    except (httpx.HTTPError, ValueError) as exc:
        logger.warning("Supabase interaction write failed: %s", type(exc).__name__)
        return False
