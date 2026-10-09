# Pilot result

Both independent agents returned exactly the nine predeclared values.
- gpt-6-luna, medium reasoning: 9/9, valid JSON.
- gpt-6-astra, medium reasoning: 9/9, valid JSON.

Payloads are stored in the model-named JSON files; prompt and expected output
were saved before the calls. No tools were used by either worker.
Cost, tokens, controlled latency: unmeasured (not exposed here).
This is a single synthetic extraction fixture, not nine independent tasks.
No general equivalence, security certification or cost saving is claimed.
No production model defaults changed. Next: held-out real retrieval and
extraction tasks plus total workflow measurements using try-tool.
