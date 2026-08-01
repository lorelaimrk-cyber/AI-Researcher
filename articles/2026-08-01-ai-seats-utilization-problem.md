---
date: 2026-08-01
pillar: economics
title: AI Seats and the Utilization Problem
prediction_logged: no
---

# AI Seats and the Utilization Problem

At a typical company that has bought AI seats, a large share of the people holding one rarely
open it, while a smaller group treats the monthly token quota like a scoreboard. Neither number
tells a partner whether the work got better.

## The claim

David Maister spent thirty years telling professional service firms the same thing: once
utilization covers its cost, more hours logged stop making a firm more profitable, and the only
lever left is the value each hour produces. Firms buying AI seats are running the identical
trade without knowing it. A seat that gets opened every day is not the same fact as a
deliverable that got better, and most firms are only tracking the one that is easy to count.

## What happened

A 2026 enterprise adoption analysis by
[ValueAdd VC](https://valueaddvc.com/blog/microsoft-copilot-enterprise-adoption-what-the-data-shows-about-real-usage-vs-hype),
citing Gartner and Forrester survey data, puts weekly active use of purchased Copilot seats at
20 to 30 percent, with daily use often under 40 percent even at firms that committed to
enterprise wide rollouts. That figure is a secondary compilation rather than a named primary
report, so treat the exact percentage as directional, not precise.

It matches the general shape of a stronger, primary number. Microsoft and LinkedIn's 2024 Work
Trend Index found that 78 percent of AI users bring their own AI tools to work rather than wait
for an employer rollout, rising to 85 percent among Gen Z employees
([Microsoft WorkLab](https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part)).
Read together, the two studies describe the same uneven start: some staff have been running AI
on their own for a year before a firm ever buys them an official seat, and once that seat
exists, a large share of the people holding one rarely open it.

The opposite pattern shows up further along the same curve. IntuitionLabs tracked a developer
named Harika Yenuga who burned through 200,000 tokens in twenty minutes on a single session,
then rebuilt her workflow and cut that consumption by 70 percent once she looked at what the
task actually needed
([IntuitionLabs](https://intuitionlabs.ai/articles/token-optimization-chatgpt-claude-costs)).
One group has not started. The other started, found the tool genuinely useful, and kept scaling
the same habit past the point where more tokens bought more value.

## Why it matters to a firm like yours

Treat the firm as a machine: inputs, people, a feedback loop, outputs. The input is a seat,
priced the same whether it gets opened once a quarter or runs all day. Maister's own formula for
a professional firm's profit runs on margin, rate, utilization, and leverage, and his argument
was never that more utilization is automatically good. Past a certain point, activation just
tells a partner that people are busy. It does not tell them the firm earns more per hour of that
busyness. An AI seat inherits the same ceiling. A high activation number says the tool got
opened. Nothing in that number says whether the output needed less editing before a partner
could send it, or whether the project shipped with fewer errors. [YOUR DETAIL HERE]

Economist Charles Goodhart made the underlying point in 1975, writing about monetary policy: a
statistical regularity tends to collapse once it becomes a target of control
([Goodhart's law](https://en.wikipedia.org/wiki/Goodhart%27s_law)). The line everyone actually
quotes, "when a measure becomes a target, it ceases to be a good measure," was coined later by
the anthropologist Marilyn Strathern, not by Goodhart himself, but the mechanism is his. Track
seat logins as the success metric, and a firm will get more seat logins. It has no built in
reason to also get better work.

Cross how often a seat gets opened against whether anyone has checked its output against an
outcome, and four situations fall out.

![Are you buying activation, or are you buying value? A 2x2 matrix crossing how often a seat gets opened against whether its output has been checked against an outcome: shelfware, the efficient specialist, token theater, and the real win.](../assets/activation-value-matrix.png)

The two boxes that get discussed are the two boxes that create no confusion: shelfware is a
budget conversation, and the real win is the case everyone is chasing. The two that actually
decide how a firm spends its year are the quiet ones either side, the specialist whose light
touch already works and never shows up as a success story, and the token theater box, which
looks identical to the real win on every dashboard that only counts logins.

## The benefit case

A firm that measures the outcome instead of the login gets two different populations to learn
from. The quiet majority who never opened the tool can be shown, concretely, what a Yenuga level
user found worth the effort, rather than told in the abstract that AI helps. The heavy users
stop being a cost line to manage down. They become a source of technique instead, since someone
who ran a workflow enough times to cut their own token spend by 70 percent has already done the
optimization work a firm would otherwise pay a consultant to redo.

## The risk case

I hold this loosely, because the right amount of measurement depends on how mature the rollout
already is. Watching outcomes instead of logins takes real infrastructure: a way to tie a
specific AI assisted task to a specific deliverable's error rate or margin, and most firms have
not built that yet. Build it too early or too heavily, and a firm can slow down a rollout that
would have found its own value faster left alone. What I trust without much reservation is
Maister's underlying claim, tested across decades of professional service firms: a metric that
stops at activity, whether that activity is billable hours or token counts, keeps getting more
activity and nothing else.

## The throughline

> An opened seat and a better deliverable are two separate facts, and a firm that only tracks
> the first one is pricing AI the same way it priced the billable hour.

## A prediction

> Prediction (2026-08-01): By the end of 2027, at least one major AEC or consulting firm will
> publicly report an AI adoption metric tied to project margin or rework rate, rather than seat
> activation or token volume alone. Confidence: medium.

## What I am watching next

Whether any vendor sells a report built around hours saved or errors avoided instead of logins
and tokens. That is currently the easiest number for Microsoft, Anthropic, and OpenAI to produce
from their own billing systems, not necessarily the most useful one for a buyer. I am also
watching whether firms start treating their heaviest AI users the way good firms already treat
their most efficient timekeepers, as a source of technique to copy, rather than a number to
explain in a budget meeting.

---

<!--
Author note, delete before publishing:
- Add one specific detail only Lorela would know where [YOUR DETAIL HERE] sits above.
- Framework image generated at assets/activation-value-matrix.png via
  scripts/make_activation_value_matrix.py, same palette as the tokenomics, IP matrix, and speed
  premium assets.
- Maister's profitability formula and billable hour critique are drawn from a secondary summary
  of "Managing the Professional Service Firm" (https://tylerdevries.com/book-summaries/managing-the-professional-service-firm/),
  not the original text directly; flag this if it matters for the final review pass.
- Run the pre-publish checklist in docs/style-guide.md before shipping.
-->
