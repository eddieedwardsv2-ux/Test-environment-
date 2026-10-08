# Source: Anthropic, "The new rules of context engineering for Claude 5 generation models"

Link: https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models
(redirects to claude.dev). Author: Thariq Shihipar, Anthropic. Published 2026-07-24. Read 2026-10-08.
It's the article behind Nate's video oz2CwrPV2Rg. **These are summaries, not quotes**: the
page was read through a fetch tool, so check the original before quoting it.

- **Over 80% of Claude Code's system prompt removed** for the Claude 5 models, with no measured
  loss on Anthropic's evaluations (their own report on their own product; not replicated elsewhere).
- **CLAUDE.md stays light:** spend it on gotchas; don't state what Claude can see from the files
  and repo. Memory is now saved automatically.
- **Progressive disclosure:** split long guidance into many files (a tree loaded at the right
  time); skills are light guides that let Claude find information when it needs it. Only
  over-constrain in highly important areas.
- **Delete duplicates and conflicts:** a rule written in two places, or two rules that disagree
  (e.g. "add docs as appropriate" vs "no comments"), should go. Tool guidance belongs in the tool's
  own description.
- **Procedures load on demand:** e.g. a verification skill referenced from CLAUDE.md, instead of
  verification steps always loaded.
- **Judgement over rules:** e.g. "follow the style of the surrounding code" replaced a hard limit.
- **Examples can narrow what the model tries;** a clear interface (e.g. a fixed list of statuses)
  often works better than long worked examples.
- **Check with `/doctor`** in Claude Code to right-size skills and CLAUDE.md.
