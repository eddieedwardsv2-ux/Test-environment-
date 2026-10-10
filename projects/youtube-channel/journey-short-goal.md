# Codex /goal — prove the journey Short production workflow

## Mission

Complete the currently **NOT VERIFIED** item:

> We have not yet produced the actual AI-OS journey Short through Nate's media-production workflow and proven that HyperFrames, Creative Claw, or another toolchain gives Charlie a professional, branded result.

Do not mark this complete because a page, storyboard, HTML mock-up, prompt, or render command exists.

The goal is a **real, reviewable vertical video file** plus evidence that the production workflow was actually exercised and verified.

## Source-of-truth inputs

Read these first:

1. `AGENTS.md`
2. `context/current-focus.md`
3. `system/capability-map.md`
4. `projects/youtube-channel/README.md`
5. `brainstorms/2026-10-09-journey-video-thesis.md`
6. `research/nate-herk/opus-5-5-video-editing-workflow--7jHXoPGnA4c-notes.md`
7. `research/nate-herk/brain/concepts.md` — Concept 46
8. `research/nate-herk/brain/rules.md` — Rule 45
9. `research/hands/tried.json` — current HyperFrames evidence

Do not redesign the story unless a verification failure forces a change.

## Story and brand lock

The Short should explain Charlie's AI-OS journey to a newcomer.

Core mental model:

`new information → Router → correct Elder → work → Chief's Desk only for real decisions → result saved/used`

Charlie remains the **Chief**.
The Router is the routing layer, not the Chief.

Use the existing **Mix** visual direction:

- Terminal: typed-title treatment and typography feel
- Kinetic: boldness, clear facts, colour changes
- Glass: first two scene ideas
- growing brain / Router / Elders / Chief's Desk visual language

Avoid generic AI-template styling.

## Mandatory Nate production loop

Execute these five stages in order.

### 1. Transcribe / timed source
Use the final narration/script/voice-over as the time-aligned source.
Every important visual beat must be traceable to a spoken beat or intentional silent beat.

### 2. Cut
Remove:
- mistakes
- dead air
- duplicated wording
- unnecessary pauses
- redundant lines that hurt a Short's pace

Do this before expensive motion work.

### 3. Plan beats
Create a beat sheet with:
- timestamp/window
- spoken line
- visual action
- text on screen
- asset/source
- brand constraint
- verification criterion

### 4. Skill / assembly
Check existing capabilities before adding anything.

Use the smallest suitable media path.

Potential candidates already known:
- HyperFrames: tested at draft title-card level, verdict `later`
- Creative Claw: routed but not yet connected/tested
- other existing connected/generation/editing tools if they fit better

Do not add a large permanent skill/plugin merely to finish this proof.

If a repeated visual preference emerges, capture only the smallest reusable rule/skill needed.

### 5. Verification loop
The first render is a draft.

For every render:
1. inspect the actual rendered video;
2. inspect representative frames/screenshots;
3. check audio, timing, text, framing and branding;
4. record defects;
5. revise;
6. render again.

There must be **at least one verification-driven revision** unless the first render genuinely passes every criterion; if that happens, record the evidence for every criterion rather than simply asserting it.

## Required deliverables

Create a dedicated project folder if one does not already exist:

`projects/youtube-channel/videos/ai-os-journey-short/`

Minimum outputs:

- `brief.md` — audience, story, locked brand direction
- `script.md` — final spoken script
- `beats.md` — timestamped beat plan
- `toolchain.md` — tools used, why each was chosen, what existing option it replaced/did not replace
- `verification.md` — render-by-render defect and fix log
- final reviewable `.mp4` file, 9:16 vertical
- representative verification screenshots/frames
- `result.md` — final verdict and measurements

Do not commit huge temporary render caches or source assets unnecessarily.

## Quality gate

The goal is met only if ALL are true:

- [ ] A real MP4 exists and can be opened/reviewed.
- [ ] Aspect ratio is 9:16 vertical.
- [ ] The final video is appropriate for YouTube Shorts / Instagram Reels.
- [ ] A newcomer can understand the Router → Elder → Chief relationship without repo knowledge.
- [ ] Charlie is clearly the Chief; the Router is not presented as the Chief.
- [ ] Visual changes align intentionally with the spoken/timed beats.
- [ ] Text is readable at phone size.
- [ ] Typography, colour, motion and asset choices feel like one brand system rather than unrelated templates.
- [ ] No obvious dead air, accidental pauses, broken cuts, clipped audio or framing defects remain.
- [ ] The actual final render was watched/inspected end to end after the last edit.
- [ ] `verification.md` shows what defects were found and what changed.
- [ ] The chosen toolchain is recorded with actual quality/rework/time/cost evidence where measurable.
- [ ] HyperFrames / Creative Claw / another tool is not promoted as the default without evidence from this real task.
- [ ] Existing project/repo priorities were not silently rewritten to finish the video.
- [ ] No publishing action happened automatically.
- [ ] Structural repo checks relevant to changed files pass.

## Tool comparison

This is not required to become a giant benchmark.

Compare only the routes that can actually be exercised in the current environment.

At minimum record:

- chosen route
- alternatives considered
- reason chosen
- actual cost if any
- generation/render time if observable
- amount of manual rework
- defects found by verification
- whether Charlie could actually preview the result

If a candidate is unavailable because of login/credits/host limitations, record **NOT VERIFIED** for that candidate rather than fabricating a comparison.

## Verification report shape

Finish `result.md` with exactly:

### VERIFIED
- what was produced
- exact final file path
- what checks were run
- what those checks returned
- what toolchain was actually proven

### NOT VERIFIED
- anything still not proven
- why it could not be checked
- whether that remaining gap blocks using this workflow for the next real Short

If any quality-gate item remains unchecked, the /goal is **not met**.

## Codex /goal text

Use this as the session goal:

`/goal Produce and verify Charlie's real AI-OS journey Short using the five-stage Nate media workflow. Do not finish until a reviewable 9:16 MP4 exists, the timed beat plan and toolchain receipt are saved, the rendered artifact has been inspected and revised from verification findings, every quality-gate checkbox in projects/youtube-channel/journey-short-goal.md is evidenced, and result.md ends with VERIFIED / NOT VERIFIED. If a tool is unavailable, use the best existing route and record the limitation rather than stopping or claiming it was tested.`

## Completion rule

The worker builds.

The checks judge.

Do not let the same statement serve as both evidence and verdict.

If the environment cannot generate or inspect a real video, report the exact blocker and leave the goal NOT MET.
