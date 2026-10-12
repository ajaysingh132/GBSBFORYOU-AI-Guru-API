# API launch-readiness checklist

## Current implementation

- FastAPI routes: `/v1/health`, `/v1/teach`, `/v1/diagnose`,
  `/v1/assess`, `/v1/remediate`, and `/v1/mastery`.
- Request validation is provided by Pydantic.
- The current decision engine in `app/core.py` is deterministic and
  rule-based. It is a contract scaffold, not a generative AI teacher.
- The `provider` field currently labels the requested provider; it does
  not call OpenAI, Gemini, Hugging Face, or Floot.
- No student records are persisted by this service.

## Required before production use

- [ ] Integrate the reviewed AI Guru Brain v0.8 engine and its CBSE XII
      Computer Science adapter, RAG, source registry, and citation logic.
- [ ] Add a provider-neutral model adapter with timeouts, bounded retries,
      token limits, and safe error handling.
- [ ] Verify every retrieved curriculum claim against the source registry;
      never fabricate citations or claim mastery without evidence.
- [ ] Add authentication, authorization, rate limiting, and abuse controls.
- [ ] Add request IDs, privacy-aware logs, monitoring, and usage limits.
- [ ] Configure secrets in the deployment platform; never commit API keys.
- [ ] Run the automated tests and a staging smoke test against the deployed URL.
- [ ] Connect School OS only after API contract and authentication are agreed.

## Deployment

The repository contains a Vercel configuration, but this file alone does not
prove that a deployment exists or is healthy. Confirm the active Vercel project,
authorized account/team scope, environment variables, and deployment logs before
announcing a live API.

## Data separation

The AI Guru curriculum/teaching knowledge base must remain separate from
political, social, and economic research knowledge bases. Do not replace or
delete the v0.8 source files or curriculum chunks during integration.
