# Research experiment 1 — genuinely free AI software (2026-10-12)

## Verdict
**Research/licence documentation verified in scoped configurations; local runtime and output parity NOT VERIFIED.**
£0 recurring software/API fee means running locally on existing equipment; no claim of zero electricity, replacement hardware, labour, hosting, or universal commercial rights.

## Selected source comparison
AI Impact: `research/ai-impact/videos/jWYzTLUEk7g.md` local Ollama chat worked but coding performed poorly on older hardware (captions, creator's report). `research/ai-impact/videos/fF_sJGILBX8.md` local durable knowledge layers. Slides not captured.
Nate: `research/nate-herk/lesson-smallest-context.md` selective context, avoid context bloat, measured tests.
The Next New Thing: `research/the-next-new-thing/replace-suno-ai-chatgpt-perplexity-lovable-manus-opus-clip--GZtLsvklYBI-transcript.md`; `free-llm-for-building-agents-images-etc--ANJTdT0Ggrw-transcript.md` — paid/free backend distinctions; commercial model licensing; promotional free quotas unsuitable for unrestricted production.

## Upstream primary-source checks
- Ollama MIT software: https://github.com/ollama/ollama/blob/master/LICENSE ; runtime model licence separate.
- Open WebUI local and offline needs fully local embedding/inference: https://docs.openwebui.com/tutorials/maintenance/offline-mode/ ; https://docs.openwebui.com/getting-started/quick-start/
- whisper.cpp MIT, local transcription: https://github.com/ggml-org/whisper.cpp/blob/master/LICENSE ; https://github.com/ggml-org/whisper.cpp
- FFmpeg LGPL/GPL depending build: https://www.ffmpeg.org/legal.html
- Piper MIT software but upstream archive and voice licence concerns: https://github.com/rhasspy/piper/blob/master/LICENSE.md ; https://github.com/rhasspy/piper
- Activepieces core MIT, enterprise commercial: https://www.activepieces.com/docs/about/license
- Invoke local free, weights licences differ: https://github.com/invoke-ai/InvokeAI ; https://github.com/invoke-ai/InvokeAI/blob/main/LICENSE-SDXL.txt
- n8n Community free self-host, commercial use constrained: https://support.n8n.io/article/can-i-use-your-license-for-my-use-case ; https://github.com/n8n-io/n8n-docs/blob/main/docs/deploy/host-n8n/community-edition-features.md

## Tested classification (10 candidates)
PASS for scoped no-fee local operating path: whisper.cpp, FFmpeg, Activepieces core (3).
CONDITIONAL: Piper, Ollama+Open WebUI, Invoke, n8n Community (4).
FAIL strict unrestricted production/persistent-free test: provider-free-quota FreeLLMAPI, Voice Studio default non-commercial model, paid-agent backend (3).
PASS does not assert live installation, commercial output permissions for every model, or feature parity.

## Static verification performed
Python decision-logic assertions **8/8 pass**: all candidates classified; no free quota marked full pass; all model-dependent candidates conditional; n8n conditional; paid backend excluded; two deterministic local tools pass; no cloud-forever promise; no performance parity inferred from licence.
This is a classification-consistency check, NOT 8 application runtimes or 10 complete licence audits.

## Practical test plan
1. Record test machine CPU/RAM/GPU/OS, versions, energy and baseline requirements.
2. Install whisper.cpp; transcribe 3 licensed 3–5 minute clips; compare against independent corrected references, measure WER, runtime, memory and external network connections. Accept no paid API/network endpoint and WER <= 15% on clean speech; threshold is a pilot target, not observed.
3. FFmpeg: 5 deterministic crops/encodes/captions, verify exact duration, aspect ratio 9:16, audio playback, subtitle timing and no visual defects. Accept 5/5.
4. Activepieces: run 5 sample input→draft workflows without commercial nodes, verify 5/5 correct and zero paid endpoint requests.
5. Ollama and Open WebUI: fixed 10 question set compared to a strong baseline, source checks and useful completion. Do not claim equivalence without measurable parity; inspect licence of downloaded weights.
6. Invoke/Piper: sample output, hardware utilisation and exact applicable weight/voice permissions; reject commercial deployment absent terms.
7. n8n: confirm workflow use fits Sustainable Use License before deployment.
8. Save receipts (commands, version hashes, network evidence, source terms, actual outcome) and promote only tested scope.

No user hardware tested; no packages installed; no API paid; no changes to AI OS architecture.
Result: **RESEARCH COMPLETED / RUNTIME NOT VERIFIED**.
