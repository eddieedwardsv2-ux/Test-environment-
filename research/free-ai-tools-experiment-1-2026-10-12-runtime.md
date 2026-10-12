# Genuinely free AI alternatives — upstream refresh and runtime evidence
Date: 2026-10-12. Scope: append-only follow-up to `research/free-ai-tools-experiment-1-2026-10-12.md`. NO AI-OS redesign.

## Verified upstream references
- whisper.cpp source and MIT: https://github.com/ggml-org/whisper.cpp — CPU-capable local inference; accuracy not independently tested.
- FFmpeg: https://ffmpeg.org/legal.html — LGPL/GPL depending configured build, some components and codecs introduce other obligations.
- Ollama: https://github.com/ollama/ollama ; Open WebUI https://docs.openwebui.com/ — local path requires local downloaded models; licence/hardware and model performance vary.
- Activepieces core: https://www.activepieces.com/docs/about/license — MIT core, commercial enterprise components.
- Invoke: https://github.com/invoke-ai/InvokeAI — Apache-2.0 application; actual downloaded model licences separate.
- Piper: old https://github.com/rhasspy/piper **archived 2025-10-06**; active successor https://github.com/OHF-Voice/piper1-gpl **GPL-3.0**, and voice licences vary. Do not describe active Piper as MIT.
- n8n: https://docs.n8n.io/sustainable-use-license — community self-hosting free in permitted uses; not unrestricted open-source licence.

Additional relevant free local options checked:
- LosslessCut https://github.com/mifi/lossless-cut — open source GPL-2.0, free official direct download; store distribution may be paid.
- Shotcut https://shotcut.org — free open-source desktop video editor.
- paperless-gpt https://github.com/icereed/paperless-gpt — MIT self-hosted companion; local model config required. Not tested.

## Creator comparison
- AI Impact reports simple Ollama local chat but poor coding performance on older hardware: `research/ai-impact/videos/jWYzTLUEk7g.md` (caption-derived, not independently replicated).
- Nate Herk stresses selective context and end-to-end verification: `research/nate-herk/lesson-smallest-context.md`.
- The Next New Thing markets subscription replacements but itself describes commercial voice limits and free API quota restrictions: `research/the-next-new-thing/replace-suno-ai-chatgpt-perplexity-lovable-manus-opus-clip--GZtLsvklYBI-transcript.md`, `free-llm-for-building-agents-images-etc--ANJTdT0Ggrw-transcript.md`.
- Explicitly excluded: free provider quota multiplexers as guaranteed forever-free production backends; default non-commercial models in client work; AI products needing paid model credits, infrastructure or APIs.

## Actual runtime test — completed
Environment contains FFmpeg 7.1.5-0+deb13u1 and ffprobe. Created five **synthetic** two-second H.264/AAC clips from lavfi test video and generated sine audio, using ffmpeg, with no paid API. Verified through ffprobe 5/5 files had 320×568 portrait dimensions, 2.000 s duration and a 48000 Hz AAC audio stream. Each took 0.45–0.53 seconds of execution in this run. SHA-256:
1. clip_1.mp4 59b89eecee19fef12ba8201d5e35e06f71f850a72230870b2b60d8e7b16a19e3
2. clip_2.mp4 a3def9759182825b8ca28b85c648b689fca418604950dba4013988baa7540ca0
3. clip_3.mp4 2f73f9c0e390a8fb2ea779b44e5ae68926c07a47a65cf744e1a7901aa9262f53
4. clip_4.mp4 310072184f2996cf6fff51465aa699490b2403625da56ac8b5757cb033762c53
5. clip_5.mp4 7791be2c2ecc75f5e683149c4ee242d1313a70ed882fa2f4d957a6745d445b35

Generated files and execution script live in session workspace /mnt/data/free-ai-exp1/ (not GitHub binaries). Results are reproducible using the script `test.py` stored in that folder in the session, but NOT portable to a later GitHub-only session unless copied separately. Network was not used by FFmpeg command; no paid endpoints invoked. Tests do not cover captions, automatic clip selection, footage quality, mobile playback or commercial use of audio.

## Blocked transcription
whisper-cli not installed. Attempt to fetch https://github.com/ggml-org/whisper.cpp.git via git ls-remote failed with 'Could not resolve host: github.com'. Thus 0/3 transcription tests and no measured WER or latency. No installation, download, model quality or network policy verified.

## Next verified production test
1. On a machine with GitHub access, use official whisper.cpp README to build, download a model with verified licence and test three licensed speech clips against human-corrected references; record WER, RAM, latency and network calls. Accept <=15% WER on selected clear speech fixture (goal, not a universal quality guarantee).
2. Edit five real authorised clips and check 9:16 framing, subtitle timing and mobile playback; independent human review.
3. Recheck actual hardware, licence and version of each finalist before describing a business deployment as permanently free.

STATUS: **UPSTREAM DOCUMENTATION REVIEWED; FFMPEG SYNTHETIC VIDEO TEST VERIFIED 5/5; COMPLETE VIDEO PIPELINE NOT VERIFIED; WHISPER NOT VERIFIED; NO PROVEN PAID-TO-FREE QUALITY PARITY**.
