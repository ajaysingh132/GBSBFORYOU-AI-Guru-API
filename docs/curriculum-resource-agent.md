# GBSBFORYOU Curriculum Resource Agent v1.0

## Purpose
Collect, validate, organize, and expose educational resources for the GBSBFORYOU AI Guru. The agent is a resource pipeline, not an authority that automatically declares every collected item correct.

## Source tiers
1. **Curriculum authorities**: official NCERT, CBSE, state/central education bodies, and other designated curriculum authorities. These define syllabus coverage and expected learning outcomes.
2. **Institutional open education**: university/open-course repositories and research/teaching institutions. Use as supplementary explanation and enrichment.
3. **Community-discovered resources**: public Telegram channels/groups and user-provided links. Treat as unverified leads until provenance, accuracy, relevance, and reuse permissions are checked.

Do not treat a public link or a free download button as permission to republish or redistribute. Record licence/terms when known; do not bypass access controls, paywalls, Telegram membership restrictions, robots/rate limits, or copyright restrictions.

## Pipeline
1. Discover URLs from an approved source registry.
2. Fetch only public/authorized resources using conservative timeouts, size limits, and rate limits.
3. Preserve original file bytes unchanged and calculate SHA-256.
4. Extract metadata: title, author/institution, URL, retrieval time, class, subject, syllabus session, chapter, language, file type, licence/terms, and extraction status.
5. Validate file type and parseability; quarantine malformed, executable, encrypted/unreadable, duplicate, or suspicious files.
6. Extract text into a separate derived artifact; retain page/section boundaries for citations.
7. Compare resource metadata against the curriculum map. A resource must not be marked curriculum-aligned solely because a filename contains a subject name.
8. Assign review state: `discovered`, `downloaded`, `needs_review`, `verified`, `rejected`, or `superseded`.
9. Index only approved, parseable resources for retrieval. Every retrieved chunk must carry a source ID and page/section locator.
10. In teaching responses, distinguish syllabus-core material from supplementary/enrichment material and return source citations where available.

## Validation principles
- Separate factual correctness from editorial interpretation.
- Confirm important claims against independent, credible sources where feasible.
- Record disagreements and uncertainty instead of silently resolving them.
- GBSBFORYOU analysis may contextualize evidence but must not alter source facts to fit a preferred conclusion.
- Do not claim a resource is "verified" unless a review event records who/what checked it, when, and against which evidence.
- Never claim student mastery without assessment evidence.

## Storage layout
- Original artifacts: object storage (e.g. configured Supabase Storage or another authorized store); do not put large PDFs or private credentials in Git.
- Metadata/source registry: database table(s) or a versioned JSON manifest for initial local testing.
- Extracted text/chunks: a separate searchable store, each chunk linked to source ID, file hash, and page/section.
- Secrets: environment variables or secret manager only. Never commit API keys or Telegram bot tokens.

## Suggested metadata fields
`source_id`, `canonical_url`, `title`, `author_or_institution`, `source_tier`, `class_level`, `subject_code`, `subject_name`, `session`, `chapter`, `language`, `mime_type`, `sha256`, `retrieved_at`, `licence_or_terms`, `review_status`, `review_notes`, `extract_status`, `page_count`, `supersedes_source_id`.

## Telegram connector
Telegram is a discovery channel, not an automatic trust signal. Prefer public channels and files that are authorized for access and reuse. Save the message link/channel name and original attribution when available. Treat posted files as untrusted input; never execute embedded files or macros. Do not attempt to access private groups/channels without authorization. Use Telegram's official API and comply with its terms and rate limits.

## Free-first operating policy
- No paid model/provider is required for collection, metadata, hashing, basic PDF text extraction, or local tests.
- Do not invoke paid inference APIs during resource collection.
- Make provider/model calls opt-in and explicitly configured.
- Use strict download limits and avoid unnecessary repeated downloads.
- Report storage and service free-tier limits instead of promising unlimited free operation.

## API/RAG integration contract
The retrieval layer should return structured evidence:
- source ID and title
- canonical URL
- source tier and review status
- page/section locator
- relevant excerpt
- syllabus alignment (core, supplementary, unknown)
- extraction/retrieval warnings

The AI Teacher must not cite a source it did not retrieve. If no approved evidence is found, it must say that source-grounded evidence was not available and either ask for clarification or give a clearly labelled general explanation.

## Staged rollout
1. Source registry and metadata validation.
2. Authorized downloader and file integrity checks.
3. PDF/HTML extraction with page/section citations.
4. Chapter-wise coverage audit against Class XII subject maps.
5. Retrieval tests with known-answer questions.
6. Add Telegram connector only after source registry and review workflow are operational.
7. Integrate with AI Guru routes on a separate branch; run tests and staging checks before production deployment.

## Acceptance criteria
- Each stored resource has provenance and a stable hash.
- Duplicate files are detected by hash.
- Unreadable/unsupported files are marked rather than silently accepted.
- No secret is stored in Git.
- Retrieval evidence always includes a source ID and locator.
- Core syllabus sources are distinguished from supplementary sources.
- Unsupported claims and conflicting evidence are surfaced.
- Existing API response contracts remain unchanged unless a versioned change is approved.
