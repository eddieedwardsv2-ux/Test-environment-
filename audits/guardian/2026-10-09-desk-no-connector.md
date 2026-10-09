**READY**

Guardian report on the connector-free Desk: Send (or Tell Claude now) saves `poke.json` inside the Desk through its own `artifact` capability, republishing it and waking Claude sessions that watch it. Saved in short, close to its words.

**Notes:** the success line "Claude has been told" claimed more than a publish proves (fixed after this report: "The Desk pinged any open Claude session; if none is open, the next one reads it"); the retry button showed after permanent codes such as `capability_disabled` (fixed: no button for permanent codes); after a `conflict` the view reloads, but the answered card's own button still works; the Codex line in the `decide` skill was muddled (reworded); two rebuilt maps were unstaged and behind (republished in this commit).

**VERIFIED:** 6 files staged; no `mcp`, `config/session` or `callTool` left in the Desk; `use("artifact")` loads after the questions with errors caught; `art.publish({"poke.json": ...})` is the files form, matching artifact.d.ts, and the error codes checked all exist; the answer is saved before any tell; script parses; `poke.json` valid; `published.json` fingerprint matches; the skill says watch at session start, cards are the record, Codex fallback; pages.md and decisions.md updated; audit 0 errors.

**NOT VERIFIED:** the live wake (nobody has pressed the button yet); the live version and capabilities; whether the files form is available on this artifact; the watch list; the deleted `config/session` doc.

**Pleasing check:** only the success wording, now fixed.
