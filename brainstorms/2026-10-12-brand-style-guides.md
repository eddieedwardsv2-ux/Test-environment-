# Three draft style guides for Charlie's AI/education outputs

Written 12 October 2026. Status: **DRAFT FOR REVIEW**. Research is exploratory; no guide is activated as a default. User selected AI/education brands. Keep Charlie's plain UK English, useful detail, connected prose and clear next action. Avoid hype and fragmented one-line writing.

## What the research supports

Kurzgesagt and Veritasium are the largest of this seven-brand shortlist. AI Explained has the highest measured median public interaction ratio among the five with available likes/comments in this selected sample. These are different measures. They do not establish the world's largest/most engaged brands, trust, retention, conversion or causality.

| Brand | Subscribers, rounded | Median views, 10 selected uploads | Median (likes + comments)/views | Sample publication range |
|---|---:|---:|---:|---|
| Kurzgesagt | 25.70M | 6.85M | 3.21% | Mar 10, 2026–Sep 22, 2026 |
| Veritasium | 21.30M | 6.55M | 2.51% | May 3, 2026–Sep 21, 2026 |
| 3Blue1Brown | 8.68M | 1.55M | 3.11% | Sep 18, 2025–Sep 18, 2026 |
| Fireship | 4.29M | 2.35M | 1.34% | Aug 27, 2026–Sep 21, 2026 |
| Nate Herk | 1.06M | 71K | Unavailable | Sep 9, 2026–Sep 19, 2026 |
| Matt Wolfe | 1.02M | 156K | Unavailable | Aug 26, 2026–Sep 22, 2026 |
| AI Explained | 0.46M | 119K | 3.81% | May 29, 2026–Sep 16, 2026 |

Sources: [Kurzgesagt](https://prepublish.ai/youtube-channel/kurzgesagt), [Veritasium](https://prepublish.ai/youtube-channel/veritasium), [3Blue1Brown](https://prepublish.ai/youtube-channel/3blue1brown), [Fireship](https://prepublish.ai/youtube-channel/fireship), [Nate](https://prepublish.ai/youtube-channel/nateherk), [Matt](https://prepublish.ai/youtube-channel/mreflow), [AI Explained](https://prepublish.ai/youtube-channel/aiexplained-official). Interaction snapshots: SPEAKRJ URLs retained with each matched row in [sample data](2026-10-12-brand-engagement-sample.json).

Selection: latest ten listed non-Shorts uploads dated on/before 22 September 2026, excluding videos over two hours. The cutoff avoids extremely fresh uploads at the oldest provider snapshot. Ages still vary widely: 3Blue1Brown's sample extends back a year. Views are rounded provider values; interactions use their own same-snapshot numerator and denominator. Nate/Matt interaction data was inaccessible, not zero. This is a consistent format/count comparison, **not a fully age-matched engagement benchmark**. Different topic markets and sampling coverage also limit cross-brand ranking.

All seven have ten selected records (70 total); five have ten matched interaction records (50 total). Video IDs are missing: title/date/count matching is provisional. We manually distinguished 3Blue1Brown's same-title/same-date Short and full video. Do not promote these rankings to verified facts without video-ID and current-source checks.

## Observations and draft hypotheses

- **Nate:** saved Karpathy teaching demonstrates defining a finish line, building a small example, predicting, running and comparing; his OS teaching routes to situational context. Use outcome-first practical demonstration. Sources: [Karpathy example, 8:05](https://www.youtube.com/watch?v=bvGptCLDhyo&t=485s), [router, 12:46](https://www.youtube.com/watch?v=Ek1NBfnnTH0&t=766s).
- **Fireship:** one inspected [caption source](https://prepublish.ai/youtube-transcript/FluKUJyeYD8) combines topical narration with jokes and a fast sequence of examples. Proposed use: tighter openings and economical transitions. Do not copy its insults, medical jokes, catchphrases or treat speed as a proven retention cause.
- **3Blue1Brown:** [neural-network captions](https://prepublish.ai/youtube-transcript/aircAruvnKk) begin with recognising a handwritten digit; the [official attention lesson](https://www.3blue1brown.com/lessons/attention) carries a concrete language example through diagrams, questions and caveats. Proposed use: one example develops with the explanation.
- **Kurzgesagt:** [asteroid captions](https://prepublish.ai/youtube-transcript/dKm7T13X7n4) use a concrete scenario, scale comparisons, unsuccessful approaches and a revised solution. Its [official site](https://kurzgesagt.org/) describes illustration/animation for approachable complex topics. Proposed use: scenario and mechanism, without manufacturing disaster stakes.
- **Matt Wolfe:** one [interview caption source](https://prepublish.ai/youtube-transcript/S2VJU5DQqlU) moves from a striking capability to what it does, who uses it, costs and an on-screen walkthrough described in speech. Proposed use: connect a tool to a real job and ask practical questions. This is not proof of its actual visuals.
- **Veritasium:** its [official site](https://www.veritasium.com/) describes experiments, interviews and demos. A [third-party script comparison](https://prepublish.ai/breakdowns/veritasium) suggests concrete stakes as a hypothesis; the comparison is observational and not independently replicated here.
- **AI Explained:** sampled titles frame documents, evidence and uncertainty; actual caption retrieval of a selected recent video failed. Treat its detailed script habits as unconfirmed, rather than inventing them from titles.

These observations are limited examples, not comprehensive creator voice analyses. No motion/thumbnail inspection completed. Colour, typography and layouts below are Charlie's proposed design choices, not extracted brand specifications.

## Shared rules for every guide

Audience: a UK beginner learning to use AI for real work. Start with why this matters to the reader. Prefer concrete nouns and verbs; explain terms when needed. Use paragraphs of two to four connected sentences for articles; lists only for true steps or comparisons. Preserve nuance, never use an arbitrary word/line limit to delete necessary information.

State what was observed, inferred and remains unknown. Link significant facts to sources. Label invented demonstrations and illustrative data. Never say we tested, measured or saved something without a receipt. Headlines must deliver the promised answer. Avoid invented credentials, revenue claims and guaranteed outcomes.

Visuals must explain a relationship, process or result. No decorative node cloud as proof of a working system. Use real screenshots for real products. Charts require units, dates and source notes. Text should remain readable on a phone, meaning must not depend on colour alone, and motion should have a reduced-motion alternative.

## Draft 1 — Practical teacher

**Purpose:** help a beginner complete one useful task. Default candidate for setup lessons and workflow tutorials.

**Voice:** warm, direct and specific. Speak as a capable colleague. Brief explanation, then show what to do and how to check it. One light aside is enough; do not make the learner the joke.

**Structure:** the problem and desired result → worked example → steps and reasons → actual check → next action. Show a failure only when it teaches the mechanism.

**Visual proposal:** light warm background, near-black text and one blue accent. Clear numbered steps, one screenshot crop per step, highlight the exact control or changed result. Prefer a human-readable file path over a crowded architecture map.

**Article adaptation:** lead with the task, include a worked example and a short finish-line checklist. **Short-video adaptation:** show the intended result first, then one main operation and its check. **Carousel adaptation:** one operation per slide; finish with a usable prompt or checklist.

**Same-topic example:**
> If your AI keeps missing notes you've already saved, start by checking where it looked. A short index can point it towards the right project, but the test is whether a new session finds the correct note and shows its source. Pick one question with a known answer, run it, and record what it reads.

**Reusable instruction:**
Write for a beginner completing [task]. Explain the useful result, demonstrate a worked example, give the necessary steps and show how to check success. Use plain UK English and connected prose. Separate actual results from suggested tests. Finish with one next action.

**Review:** can the reader act without guessing a missing step? Does the check measure the outcome rather than repeat the instructions? Is any time/cost promise evidenced?

## Draft 2 — Visual explainer

**Purpose:** make an unfamiliar mechanism understandable. Candidate for routers, agents, second brains and workflow diagrams.

**Voice:** curious, calm and clear. Begin with a concrete situation, introduce one analogy, then explain exactly where the analogy stops. Build complexity gradually.

**Structure:** familiar example → useful mental picture → mechanism → complication → practical implication. Reuse the same example rather than changing subjects each paragraph.

**Visual proposal:** ink-coloured background, white labels, cyan for retrieval and amber for decisions. Consistent colours represent consistent roles; also use labels/shapes. Draw a few meaningful elements and reveal changes gradually. Avoid copying another creator's characters or diagram styling.

**Article adaptation:** one central diagram and connected explanatory prose. **Video adaptation:** synchronise narration with the state being shown; pause after introducing a new relationship. **Slides adaptation:** retain stable object positions across successive frames.

**Same-topic example:**
> Imagine asking a librarian for one book and receiving the entire library. An AI knowledge system faces a similar problem when it loads a whole folder for a small question. The index acts as a map: it points to the relevant shelf, while the source note supplies the evidence. The map helps only if its pointers still work.

**Reusable instruction:**
Explain [mechanism] through one concrete example. Build from the familiar situation to the actual mechanism, flag the limits of any analogy and suggest one diagram that would make the explanation clearer. Use calm UK English. End with a practical implication.

**Review:** can someone explain the mechanism afterwards? Do diagram labels match the explanation? Does every animation communicate a change? Is the analogy accurate enough for this audience?

## Draft 3 — Evidence-led analyst

**Purpose:** help someone choose what to trust or test. Candidate for model/tool comparisons, research briefings and business decisions.

**Voice:** measured, curious and willing to disagree. A strong opening identifies a concrete uncertainty; it does not manufacture controversy.

**Structure:** decision/question → evidence → alternative explanation → limits → recommendation → test. Keep evidence and interpretation visibly distinct.

**Visual proposal:** warm white background, dark text, restrained teal accents. Compact comparison tables, readable source/date notes and labelled confidence or status. Use amber for unresolved questions with a written label. Avoid fake precision, dramatic scorecards and meaningless rankings.

**Article adaptation:** answer first, then support and limitations. **Video adaptation:** show the test input and result alongside the claim. **Briefing adaptation:** what changed, why it matters and the smallest worthwhile trial.

**Same-topic example:**
> A tidy knowledge base can still return the wrong answer. To judge whether the structure helps, give two setups the same questions and check their answers against known sources. Record accuracy and what each reads; measure usage only when the account exposes it. A shorter response alone tells us little about whether retrieval improved.

**Reusable instruction:**
Help decide [question]. Lead with the provisional conclusion, identify supporting evidence and the strongest alternative explanation, state the limits, and recommend one measurable test. Use clear UK English. Distinguish observed facts from inference and missing data.

**Review:** is the conclusion proportional to the evidence? Are comparators fair? Are missing data shown as missing? Could another explanation account for the apparent improvement?

## How to choose and apply

Recommendation: use Practical teacher as the initial candidate for beginner lessons; Visual explainer for mechanisms; Evidence-led analyst for comparisons. This is an editorial recommendation, not a tested engagement prediction.

Keep these as selectable guides in a project/voice file. Retrieve only the chosen guide plus necessary brand/project context. Do not load all three into every task or install a framework for them. The capability map already provides creator research, ingestion and writing routes; no paid service or new plugin is needed for these briefs.

Next validation: use the same verified topic and facts to produce one 250-word article and one 45–60-second script in each direction. Ask a small group of beginners to identify the main point, explain the mechanism and choose the next action. Record their answers. Revise confusing passages before measuring real published performance. If later published, record retention and interactions within the same format/time window; do not attribute differences to voice alone.

## Status

Research sample and three concrete briefs exist. No full brand identity selected; no guide activated; no publishing or installs performed. Public metrics remain provisional (missing IDs, varying ages/snapshots, two missing interaction datasets). Visual brand analysis, full seven-brand caption review and independent Guardian review are outstanding. Workspace audit/page rebuild unavailable after the earlier usage-limit review failure; no claim those checks ran here.

**NOT VERIFIED** — strongest-brand ranking, causal engagement benefit and runtime output quality. Drafts are ready for Charlie to compare as proposals.
