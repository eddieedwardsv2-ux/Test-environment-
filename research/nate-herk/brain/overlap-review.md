# ENATE overlap review (2026-10-09)

Read-only review of the 43 concepts and 43 rules, after the smallest-context
work (concept 39, Rule 41). Charlie chose "only fix the clashes" on the Decision Desk (2026-10-09):
Rule 19 and concept 18 are now marked as replaced by Rule 41 and concept 39.
The rest of the merge was not done.

## The biggest redundancy is by design
Each concept (an idea, with quotes) has a matching rule (what to do, with
the same quotes). Rules 31-40 repeat concepts 29-38 word for word in their
titles. So most "overlap" is the same idea written twice, on two pages.

## Real overlaps (rules)
| Group | Rules | Why they overlap | Merge into |
|---|---|---|---|
| What the always-loaded file holds | 4, 5, 19, 41 | All say: keep the rulebook small, route don't store, only expertise in it | One rule (41) |
| Session context | 29, 31 | Both: long chats rot; hand off and clear at about half the window | One rule |
| Verification | 2, 16, 33 | Fix poisoning with checks; enforce checks with a gate; a separate checker decides "done" | One rule |
| Test the real thing | 17, 27 | Test in the real setting; look at visual output before calling it done | One rule |
| Audits | 7, 8, 28, 40 | Read-only, indexes are claims, save and read the last report, score each run | One rule (the audit) |
| Evidence | 12, 13 | Raw sources untouched; no source, no rule | One rule |
| Skill life cycle | 23, 34 | Report-only until tested; one job, built from a real run, retired when unused | One rule |
| Making skills findable | 20, 22 | Register in the router; validate front matter | One rule |
| Permissions | 25, 36 | 36 already contains 25 (settings, not prompts) | One rule (36) |

43 rules → about **29**, with every quote kept.

## Real overlaps (concepts)
| Concepts | Merge into |
|---|---|
| 18 (router under 200 lines) and 3 (router, not warehouse) | 39, the smallest context that works |
| 22 and 32 (how skills are built and retire) | one skills concept |
| 24 and 34 (permissions) | one |
| 27 and 29 (session hygiene, context rots) | one |
| 40 and 41 (test a model; evals before trust) | one "measure before you trust" |

43 concepts → about **38**.

## Clashes with how we work now
1. **Rule 19 "under 200 lines" vs Rule 41 "smallest that works".** Our rulebook is
   76 lines; `tools/context_check.py` warns past 90, `tools/audit.py` still
   errors only past 200. Newer wins: 41 is the rule, 200 is just the hard ceiling.
2. **Rule 7 "audit, then wait for approval" vs "don't make Charlie a checkpoint".**
   No real clash: approval still happens, but once, on the Decision Desk.
3. **Rule 15 "turn knowledge into an agent plus a skill" vs Rule 24 "don't overuse
   sub-agents".** Mild: ENATE and the Hands Brain advisors are read-only and earn
   their place; new agents need the same test.
4. **Rule 42 "fixed flows as code"** repeats the scripts part of Rule 35, and our own
   Karpathy rule "smallest version first". Keep 42; point 35 at it.

## How to merge safely (if chosen)
Keep every quote and timestamp, move them under the surviving rule, and leave
each old number as a one-line pointer ("Rule 19: now part of Rule 41"), so
older notes and the Brain dashboard still resolve. Then `tools/audit.py`
(quote checker) must pass, and the fresh-session test must give the same answers.
