# Toolchain receipt

Task: Charlie's actual eight-scene AI-OS journey Short. Not a title-card benchmark. Source branch: `chatgpt/nate-video-editing-ingest-2026-10-10`, original goal commit `fb0b8fe`.

| Stage | Actually used | Evidence / boundary |
|---|---|---|
| Timed source | Microsoft Edge TTS, standard en-GB-RyanNeural voice, eight takes | Synthetic narrator, not Charlie's cloned voice. 149 words. `prepare_audio.py`, `timed-source.json` |
| Cut | FFmpeg outer-silence detection and trim | 7.435294 s removed; 57.733333 s timeline; retained consonant padding and natural internal breaths; no atempo or pitch shift |
| Beat plan | Existing Mix draft and thesis, explicit eight-row plan | `brief.md`, `script.md`, `beats.md`; no new brand theme or story redesign |
| Assembly | Existing Higgsfield sandbox's native Higgsedit CLI | CLI doctor passed Node, FFmpeg, native compositor and MP4 decode. H.264 1080×1920 / 30 fps; 8-bit compatible export; actual render receipts |
| Font correction | Actual JetBrains Mono 700 + DM Sans 700 WOFF2, imported as native font assets | Font-name-only legacy rendering was not sufficient. `higgsedit fonts add` verified bytes. Missing arrow glyph caused a failed shaped render; replaced decorative arrow with `FAULT TEST: CAUGHT` |
| Speech verification / final clock | Local faster-whisper small, CPU int8 | 14.425 s measured recogniser run. All 149 words recognised; raw similarity 0.993289; sole organise/organize spelling difference. `speech-check.json`, `aligned-source.json` |
| Timed text | Higgsedit native text clips on Whisper-derived clock | Packaged subtitles scripts missing; fallback required by user's explicit instruction. ≤5 words / ≤32 characters; authored wording and punctuation preserved. No success claim for packaged subtitle workflow |
| Inspection | FFmpeg decode / stream probe / silence / loudness; actual decoded frames at phone scale | Full final inspection and measurements recorded in `verification.md` and evidence files |

## Quartermaster / Architect check

HyperFrames is rank 1 for media in the existing Hands list; shown in W41, with the sourced demonstration “Agents can now write HTML and render MP4s.” Earlier actual trial: ten-second landscape title card, 14 s draft render, one overlap fixed; Charlie's verdict remains **later** because preview failed. This Short does not overwrite that verdict or claim HyperFrames was run.

Creative Claw was explicitly checked. Its skill instructions became available after continuation on 11 October, but runtime discovery still returned zero callable Creative Claw tools. No connection trial, generation, cost comparison or quality comparison is claimed. **NOT VERIFIED** for this candidate. No signup or plugin install attempted.

Higgsedit is the runner-up selected for execution because its native renderer and existing sandbox actually worked; this specific CLI is **not in the Hands ranked list** (the listed Higgsfield thumbnail skill is a different capability). It does not replace HyperFrames or Creative Claw globally. Architect: concept 46 / Rule 45 fits this five-stage production/inspection loop; tool choice remains replaceable. We tested a real Short, not a demo from memory.

## Cost, time and rework

- No paid generation tool was submitted; no credits purchased or debited by this task. Edge TTS and local/native rendering used no per-generation credit calls. Account subscription / hosting / compute costs were not measured and are not claimed to be zero.
- TTS generation/cut pipeline: 13.881 s. ASR: 14.425 s.
- Five successful exports: r1 26.813 s, r2 26.406 s, r3 91.304 s, r4 92.039 s, r5 98.927 s (CPU). Receipts: `render-r1.json` through `render-r5.json`. These are renderer wall times, not total human editing time or a controlled speed benchmark.
- Manual rework: timing-contract fix, map/label/caption layout revision, font-byte/reading-time correction, 19 caption overlap fixes, specialist-to-result connection and explicit Chief's Desk label. Five successful render passes plus pre-render failures; editing minutes were not reliably measured. No permanent skill/plugin/framework was added.
- Final encoded-audio ASR: 11.560 s, 148/149 words, similarity 0.989899. ASR omitted `it` after `document`; source ASR recognised it. PCM comparison confirms 0.999916 correlation / 37.666 dB SNR against the source over all 57.733 s, zero clipped samples; this is a recogniser discrepancy, not evidence of a missing segment. Both raw recognition receipts retained.
- Limits: not a comparative benchmark; no claim this route is cheapest or the default. Human preference, actual iPhone playback, audience retention, automated posting and the OS's overall reliability are separate tests.

## Reproduction

Scratch dependencies: edge-tts, FFmpeg, faster-whisper small, native Higgsedit. Scripts stay within this project. Reuse saved narration/timing to avoid changing voice between revisions. Recreate the fonts with `higgsedit new fontkit`, then `higgsedit fonts add fontkit "JetBrains Mono:700" "DM Sans:700"`; final build uses `JOURNEY_REVISION=5 higgsedit build edit.js`. Fast-start remux `draft-r5.mp4` to `charlie-ai-os-journey-short-final.mp4`; run `JOURNEY_REVISION=5 python3 inspect_video.py`; extract audio and run `python3 transcribe_check.py final-audio.wav speech-check-final.json`. Native project caches and temporary provider takes are not required deliverables.

Export limitation corrected: archive upload first returned HTTP 403 because its reserved MIME type was `application/octet-stream`, not the requested ZIP type. A fresh reservation with the returned MIME type succeeded HTTP 200 and was confirmed. MP4 upload succeeded HTTP 200 and was confirmed. CLI Git push is unavailable (no configured username); GitHub's existing authenticated tree/commit/ref connector is the source-save fallback, with a branch-head lease. No credentials were extracted.
