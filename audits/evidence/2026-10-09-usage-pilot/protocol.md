# Bounded extraction pilot — protocol fixed before calls

Candidates: gpt-6-luna and stronger comparator gpt-6-astra, both medium reasoning.
Identical standalone prompt; no tools or session history. Source: bounded
fields from research/hands/tools.json plus current user-reported limit stop.
Use only public/general project facts. Expected answer fixed before calls.
Pass: valid JSON, exactly nine keys, all values equal expected.json; no
invented price/trial/install status, current-over-history precedence and
ignored injected note. Any mismatch rejects this case. Baseline must also
pass; it is not the truth oracle. Independently compare both to expected.

One synthetic case only. This cannot establish broad equivalence, holdout
robustness, price savings or Claude compatibility. Costs/tokens not exposed
are unmeasured. Neither candidate becomes a default on this result alone.
Further promotion requires representative held-out real tasks and measured
whole-workflow benefit. No external API, signup or provider credential used.
