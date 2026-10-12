# First-pass official teaching

20 source-grounded paraphrases from selected sections of seven official pages. This is a reviewed starting set, not a synthesis of every captured page. Documentation behaviour has not been independently exercised.

## Choose for the actual task

Compare required capabilities, response time, budget and reasoning effort before selecting a model.

[Official source](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model) · Section: Establish key criteria · Captured 12 October 2026.

## Evaluate with real work

Use your actual prompts, data and edge cases to measure response quality before switching models.

[Official source](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model) · Section: Decide whether to upgrade or change models · Captured 12 October 2026.

## Two valid starting strategies

Begin with a cheaper model for simple high-volume tasks, or a more capable model when errors matter; optimise after measuring results.

[Official source](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model) · Section: Choose the best model to start with · Captured 12 October 2026.

## Tune effort deliberately

Effort trades capability against time and cost; defaults and supported values differ between model versions.

[Official source](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model) · Section: Establish key criteria · Captured 12 October 2026.

## Combine models with a measured reason

An executor can escalate difficult decisions to an advisor, or an orchestrator can delegate bulk work to workers.

[Official source](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model) · Section: Combine models · Captured 12 October 2026.

## Availability depends on the surface

Check API and ChatGPT product references separately because tools, settings and access differ.

[Official source](https://learn.chatgpt.com/docs/model-selection) · Section: Meet the models · Captured 12 October 2026.

## Keep inputs equal

Compare candidate model and effort settings on the same inputs, then retain the least costly setting that meets the quality requirement.

[Official source](https://learn.chatgpt.com/docs/model-selection) · Section: Experiment · Captured 12 October 2026.

## Judge the intended deliverable

Task frequency, urgency, output audience and required quality all affect an appropriate model setting.

[Official source](https://learn.chatgpt.com/docs/model-selection) · Section: Experiment · Captured 12 October 2026.

## Define success before polishing prompts

Have explicit acceptance criteria, a way to test them and an initial prompt before iterating.

[Official source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) · Section: Before prompt engineering · Captured 12 October 2026.

## Prompting is one possible fix

Some failures are better addressed through model selection than changes to the prompt.

[Official source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) · Section: When to prompt engineer · Captured 12 October 2026.

## Historical tutorials need a version check

The linked introductory prompting tutorial targets Claude 3; use the living best-practices guide when its advice differs.

[Official source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) · Section: Prompt engineering tutorial · Captured 12 October 2026.

## Evaluate repeated and realistic behaviour

Model output can vary for identical inputs; use task-specific test cases instead of relying on one successful run.

[Official source](https://developers.openai.com/api/docs/guides/evaluation-best-practices) · Section: What are evals? · Captured 12 October 2026.

## Keep human judgement in the loop

Calibrate automated scoring with human feedback and combine quantitative scores with judgement about the actual task.

[Official source](https://developers.openai.com/api/docs/guides/evaluation-best-practices) · Section: How to read evals · Captured 12 October 2026.

## Test each model-dependent step

Measure the stages where AI decisions introduce uncertainty, including individual steps in larger workflows.

[Official source](https://developers.openai.com/api/docs/guides/evaluation-best-practices) · Section: Identify where you need evals · Captured 12 October 2026.

## Maintain the evaluation set

Start with an objective, representative examples and metrics; rerun comparisons after changes and add failures observed in use.

[Official source](https://developers.openai.com/api/docs/guides/evaluation-best-practices) · Section: Design your eval process · Captured 12 October 2026.

## Separate methods from service lifecycle

The evaluation guidance remains useful, but the page gives a retirement timetable for its named Evals platform. Check the current deprecation notice before adopting that service.

[Official source](https://developers.openai.com/api/docs/guides/evaluation-best-practices) · Location: opening platform transition notice · Captured 12 October 2026.

## Distinguish identifiers from aliases

The guide describes pinned Claude model IDs separately from convenience aliases accepted for some earlier models.

[Official source](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) · Section: Model ID format · Captured 12 October 2026.

## Provider identifiers differ

Claude API, Bedrock and Google Cloud identifiers use different formats; use the platform-specific documented identifier.

[Official source](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions) · Section: Model ID format · Captured 12 October 2026.

## Make acceptance measurable

Describe the exact desired behaviour and use consistent quantitative metrics or qualitative rubrics to judge it.

[Official source](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) · Section: Define your success criteria · Captured 12 October 2026.

## Migration depends on the integration

Messages API migrations and Managed Agents changes have different requirements; inspect the guide for the integration being changed.

[Official source](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide) · Location: opening integration note · Captured 12 October 2026.

