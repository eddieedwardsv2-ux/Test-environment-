# Render verification log

## Before render

- Followed router and read exact goal on the ingest branch, not main (main returned 404). Preserved story / Mix brand lock and unrelated priorities.
- Voice stage: eight takes, 149 words, 57.733333 s after cutting 7.435294 s of outer provider padding. No speed changes. Production receipt: `timed-source.json`.
- Independent ASR: faster-whisper small, 149 expected / 149 recognised words; similarity 0.993289. Only difference: organise / organize. No missing or substituted spoken content after UK-spelling normalisation. Final caption clock uses ASR, retaining authored spelling/punctuation.
- Native build catches delayed-node lifetime overrun and absolute/local clock mismatch before any successful video output. Root cause confirmed from installed `fable.d.ts` and compiler: top-level at is absolute and omitted duration is full beat. Fix: explicit remaining lifetime and absolute placement. No project redesign.

## Draft r1 — actual rendered MP4

Native receipt: 1732 frames, 57.733333 s, CPU, 26.813 s render, zero render diagnostics; `higgsedit check` says clean. This is insufficient visual proof by itself.

Opened actual decoded scene frames (not authoring screenshots): `evidence/draft-contact.jpg` and eight `draft-scene-*.png` at 3.99, 10.29, 17.43, 24.42, 32.44, 40.85, 48.85, 55.59 s.

| Finding | Evidence | Revision |
|---|---|---|
| Multi-line role label overlaps job description | New information, Charlie = Chief, Saved result and Check result cards on draft contact sheet | Wider input/Chief cards; wider role cards; shorter job microcopy; label font bounds and separate label/job zones |
| Closing title crowds the Chief card | Scene 8 title extends into card at y570 | Graph starts at y645 below the title; Router moves to y1010, result cards y1190 |
| Captions run long and lack authored punctuation | Scenes 1, 4–8 | Re-align to independent ASR; restore authoritative punctuation; ≤5 words / ≤32 characters, 50px type |
| “Elders” definition and status strip compete for bottom map space | Scenes 7–8 | Move Elders definition above role cards; compact status text below result row |

Caption skill limitation: packaged transcription/burner scripts are absent under the advertised workflow path. The independent Whisper library is available. Charlie's explicit unavailable-tool fallback permits a native text-layer route in Higgsedit instead; no hand-rolled FFmpeg caption burn or packaged-subtitle success is claimed.

## r2–r5 — verification-driven changes

| Pass | Actual inspection / check | Finding and next change |
|---|---|---|
| r2 | Eight decoded scene frames, phone-scale opening/tools/closing views | Layout fixed; legacy fallback font rendering still malformed. Import actual font bytes; shorten closing title; guarantee final card reading time |
| r3 | Shaped decoded parts/tools/closing frames and caption interval analysis | Native fonts fixed visual quality. 19 brief phrase overlaps remained; clamp each caption end to the next start |
| r4 | Full encoded-video technical check and phone-scale map frames | Caption overlap count zero. Saved-result line bypassed the specialist; Chief label did not explicitly name the Desk |
| r5 | Full decode, encoded-audio ASR, PCM comparison, 132 decoded frames across the complete timeline, all eight phone frames | Specialist now leads to saved result; Chief card says `Desk: real choices`. No further visual correction identified in this inspection |

## Final inspection — r5, after the last edit

File: `charlie-ai-os-journey-short-final.mp4`, SHA-256 `4916c510a4f8dc156d096f78c18fcbfcdf2f164c555d9a2fff3d204bda88dc4f`. Downloaded file matches this measured export.

- Native renderer: success, 1732 frames, 98.927 s, CPU, diagnostics/fallbacks empty.
- FFprobe: H.264 High / yuv420p, 1080×1920, nominal 30 fps; AAC-LC 48 kHz stereo. Container 57.736 s, video 57.735352 s, audio 57.733 s; A/V end difference 2.352 ms. 6,618,133 bytes; fast-start remux.
- Entire encoded file decoded with FFmpeg: exit 0, no decode errors. All 41 caption intervals preserve all 149 authored words, ≤5 words / ≤32 characters, zero overlaps.
- Inspected actual decoded frames end to end: nine `evidence/final-sequence-*.jpg` sheets, 132 frames at every 0.5 s plus immediately before/after each cut and 57.65 s. Every sheet was returned and viewed; one oversized two-sheet request failed and was repeated as separate successful inspections. This is sampled end-to-end inspection plus full decode, not a claim of real-time human playback or every-frame visual judgement.
- Inspected all eight `evidence/final-phone-*.jpg` images at 390×694. Main titles, captions, role labels and job labels readable; no title/card or label/job overlap. Decorative small metadata is secondary, not required to understand the story. Foreground stays within conservative top/bottom/right app-UI margins; exact live platform overlays were not tested.
- Map: new information visibly passes through Router; Elders explicitly defined as specialists; Architect organises / Quartermaster picks tools; Charlie clearly separate as Chief with the Desk for real choices; specialist connects to usable saved result. Newcomer clarity is this reviewer's content/layout assessment, not a user study.
- Audio: -16.4 LUFS integrated, 2.0 LU loudness range, -4.3 dBFS stereo true peak; zero clipped decoded samples. Silence detector found eleven 0.972–1.020 s sentence/phrase pauses. They match intended punctuation/holds, not broken cuts or missing passages. 7.435294 s of outer provider padding already removed before motion work.
- Encoded-audio ASR returned 148 words, omitted `it` after `document`, and used US spelling `organize`. Source recognition had all 149. Entire decoded mono waveform compared with original: 2,771,200 samples, correlation 0.999916, SNR 37.666 dB, no timing offset or dropped segment. Preserve the raw discrepancy rather than claim 149/149 final ASR. Audio verification used recognition and signal analysis; human headphone listening is not claimed.
- No social upload, public post, tool-default change or priority reorder was made. Review-file hosting and requested source-save are delivery actions, not channel publishing.

## Structural checks and independent-review boundary

Changed-file link/content checks: `python3 tools/check_links.py` returns 0 errors, 0 warnings, 0 broken links; Python scripts compile; `git diff --check` clean. Caption preservation/non-overlap, source/export hash and renderer/decode assertions passed.

Full `tools/audit.py` baseline: 10 errors, 0 warnings after new routing links were added. Nine historical commits lack Guardian checks; local `.agents/skills` was already deleted on continuation and is preserved as an unrelated change. This task's multi-file production commit additionally requires independent Guardian review. AGENTS.md explicitly forbids Codex self-certification: leave that error and hand the commit to the next Claude session. The structural gate remains open; no fabricated Guardian receipt.

`tools/pages_status.py --build` ran once in an isolated copy to protect unrelated/generated files: all builders completed; five stale pages (Quartermaster, Architect/Nate, Reading Room, Brain dashboard, Nate-first map). This environment has no Artifact publishing connector, so those were not republished or marked current.

Post-source-save audit: production commit `1bb636f9806eb9d8cd2247ca98ce109974d6bf49`, 31 changed files, saved through authenticated GitHub connector with expected-head guard. Fetched remote tree matches staged source tree exactly (`71e0b23d7997dbeaba50d87178ae078fafde2ddc`). Full audit now returns **11 errors, 0 warnings**: 10 pre-existing findings plus this production commit's missing independent Guardian review. User's two unrelated local symlink deletions remain unstaged and were not published.

## Further pre-delivery findings

- r2 full-size decoded frames exposed legacy fallback typography; font names alone did not supply the expected font bytes. Actual JetBrains Mono / DM Sans assets were added and natively verified. r3's first shaped render failed on the decorative arrow glyph; that failed attempt was not delivered. The status label was changed to plain `FAULT TEST: CAUGHT`.
- The fourth agent-parts card and final specialist card had less than a second to read after their spoken noun. Revised reveals give at least 1.3 seconds; the early part of that reveal is an intentional anticipatory visual beat.
- An independent caption interval check found 19 overlaps in the earlier clock; r4 clamps each phrase's end to the next phrase's start. Full final caption coverage and non-overlap assertions must pass before delivery.
- Pre-existing repository audit baseline on 11 October: 10 errors (nine unchecked historical commits, plus the local missing `.agents/skills` link), five routing warnings. New folder/index routes are being fixed; unrelated deletions are preserved. A failed full audit will not be described as clean.
