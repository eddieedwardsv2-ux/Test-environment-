# Higgsfield (AI video, images, thumbnails)

Researched 2026-10-09. Paid credits; sign-up and connection are Charlie's call.

## Ways in (best first)
1. **Custom connector in claude.ai** (works on phone, web and in cloud sessions):
   Settings → Connectors → Add custom connector, URL `https://mcp.higgsfield.ai/mcp`,
   then sign in to Higgsfield. Tested 2026-10-09: the server answers and asks
   for sign-in (OAuth with automatic client registration, which claude.ai
   connectors use). It is Higgsfield's own server but not in Anthropic's
   connector directory, so check what it can do after connecting. Connectors
   load when a session starts: start a new session after adding it.
2. **Official skills** (`github.com/higgsfield-ai/skills`, MIT, v0.13.0, 8 skills:
   generate, soul-id, product-photoshoot, brandkit, marketplace-cards, websites,
   video-explainer, youtube-thumbnail). Need the Higgsfield CLI and
   `higgsfield auth login` (browser sign-in), so best on the Mac:
   `npx skills add higgsfield-ai/skills` or, in Claude Code,
   `/plugin marketplace add higgsfield-ai/skills` then `/plugin install higgsfield@higgsfield`.
   Install only after Charlie's OK (Decision Desk), into this project.
3. **CLI alone**: `npm install -g @higgsfield/cli`, `higgsfield auth login`,
   e.g. `higgsfield generate create nano_banana_2 --prompt "..." --wait`;
   `higgsfield account` shows credits.

## Most useful for Charlie
`higgsfield-youtube-thumbnail` (thumbnails and vertical covers for the channel)
and `higgsfield-generate` (images and short video clips). Nate uses Nano Banana
(available through Higgsfield) for diagrams and thumbnails.
