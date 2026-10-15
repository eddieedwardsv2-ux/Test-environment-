# Yarchi (@undefinedKi)

X account that turns new AI papers, repos and launches into step-by-step
threads. Also runs **Second Brain OS**, an open-source guide and starter vault:
site https://secondbrainos.dev, repo https://github.com/undefined-ui/second-brain-os
(his "9 million people read my second brain article" post, 11 Oct 2026).

Recent posts: [x-posts.md](x-posts.md) (fetched 2026-10-15 with
`research/get_x_posts.py yarchi undefinedKi`).

## Newest post checked (15 Oct 2026): OpenUI and generative UI

- Post: https://x.com/undefinedKi/status/2110756108088336637 (quotes the
  OpenUI 1.0 launch by Rabi Shanker Guha, CEO of thesysdev).
- Starts from Karpathy's 2 Oct post (in `research/andrej-karpathy/x-posts.md`):
  reading model output is the hard part, so ask for a diagram, then HTML.
- The "paper" in the image is a one-page **technical note written by Yarchi
  himself**, "compiled from the OpenUI repository, documentation and published
  benchmarks". It is not peer reviewed and has no independent experiments.
  The 58% (vs json-render) and 52% (vs A2UI) token savings are OpenUI's own
  published numbers; the repo README says "up to 67% fewer tokens than JSON".
  Neither has been checked here.
- The post's line "that is where the paper got its gain" (fetch data first,
  draw the UI last) is not backed by a result in the note: the note shows the
  order in its diagram but reports no measured gain from it. NOT VERIFIED.
- Repo: https://github.com/thesysdev/openui (MIT). For developers building
  their own app; not installed or tried here.

## How it relates to this OS

- Second Brain OS is the same raw → wiki pattern as Karpathy's LLM Knowledge
  Bases post and our `research/<creator>/brain/` folders, plus a projects layer
  like our `projects/`.
- What we already do instead of OpenUI: Claude Artifacts (Chief's Desk,
  TRADEFLOW page) are "answer in HTML" pages.
- Ideas worth borrowing (not adopted yet): a scheduled lint/health check on
  the brains; filing good answers back into the brain; a fixed set of page
  "components" for Artifacts so every page looks and behaves the same.
