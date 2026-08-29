---
date: 2026-08-29
pillar: economics
title: What AI Can't Sign
prediction_logged: no
---

# What AI Can't Sign

A colleague described how his firm used to get an urgent message to Iran before email existed. A project director wrote it by hand, someone typed it, it flew out for three days, reached the firm's Iran office, went by boat to the shore, and came back as a spoken answer someone wrote down on the other end.

[YOUR DETAIL HERE: confirm the decade and whether this was your colleague's own project, so the anecdote is exact]

Six people, one sentence, several days. Email didn't speed that process up so much as delete five of those six roles at once, the ones that existed only to move information between two points.

The same deletion is happening again inside engineering and consulting firms. This time three of the largest firms in the world have put a number on it.

McKinsey now takes about 25 percent of its global fees on an outcome basis rather than time and effort, according to Michael Birshan, the firm's UK managing partner. Its internal AI tool, Lilli, runs more than 500,000 prompts a month and is producing up to 30 percent time savings on knowledge work, and McKinsey restructured partner compensation to absorb the revenue volatility that comes with charging for outcomes instead of hours ([AI Weekly, citing Wall Street Journal reporting](https://aiweekly.co/alerts/mckinsey-ties-25-of-fees-to-outcomes-as-ai-erodes-billable-hours)). BCG expects AI-tied work to reach roughly 40 percent of revenue in 2026, up from about 20 percent in 2024. Bain puts AI and technology-enabled work at roughly 30 percent of its business now, aiming for half (same source). Those last two are self-reported figures from media events, not audited numbers, so I'd treat the precise percentages as directional rather than exact.

The mechanism behind that shift is well studied outside consulting. David Autor and Neil Thompson at MIT looked at what happens to wages once part of a job gets automated, and found it depends entirely on which part. Bookkeeping is the clean example. Once computers took over the routine side of it between 1980 and 2018, employment in the role fell by a third, but real wages for the bookkeepers who remained climbed nearly 40 percent, because what was left required judgment. Taxi driving went the other way. GPS automated the one thing that used to separate an experienced driver from a new one, street knowledge, and the job got more crowded and paid less ([MIT Sloan, on Autor and Thompson's research](https://mitsloan.mit.edu/ideas-made-to-matter/a-new-look-how-automation-changes-value-labor)). A fee that moves from hours to outcomes is a firm betting it sits on the bookkeeper side of that line.

Structural, civil, and geotechnical engineering have something the taxi industry never had: a legal floor under the differentiator. The American Society of Civil Engineers' Policy Statement 573, adopted July 18, 2024, states that AI cannot serve as a replacement for the professional judgement of a licensed Professional Engineer, and cannot be held accountable for it ([ASCE, Policy Statement 573](https://www.asce.org/advocacy/policy-statements/ps573---artificial-intelligence-and-engineering-responsibility)). That is not a norm a firm could quietly drop once a model gets good enough. It is a licensing requirement. Someone with a stamp and a license number has to review the work against the actual site, take personal liability for it, and sign. GPS never had a law protecting a driver's local knowledge. A PE's signature has one.

AECOM is already pricing around that gap. Baird's analysts, downgrading the stock on valuation rather than fundamentals, noted that AECOM estimates every 1 percentage point of labor savings adds about 20 basis points to margin, and that its AI strategy is far enough ahead of peers to support its stated margin targets through 2029. The same note flagged that AECOM's heavy mix of time-and-materials contracts puts direct pressure on billable hours, the same pressure pushing McKinsey toward outcome pricing ([Yahoo Finance, on Baird's AECOM and Jacobs downgrade](https://finance.yahoo.com/news/aecom-jacobs-downgraded-uncertainty-over-175840515.html)). Time and materials bills for hours worked. Fixed fee and outcome pricing bill for what the signature backs. Once the routine hours compress, one of those models keeps the margin, and the other hands it back to the client automatically.

Whether that judgment premium is holding up inside firms right now, not just in theory, has some early evidence behind it. A field study of 713,564 prompts from nearly 4,000 employees at one large firm, across 15 functional areas over eight months in 2025, found that sophisticated AI use tracked closely with seniority, and that formal training produced no lasting gain for anyone who went through it ([arXiv, Sophistication in GenAI Use: Field Evidence from a Large Firm](https://arxiv.org/abs/2608.27364)). If AI had already closed the gap between a junior and a senior user, that finding would look different. Right now it does not.

None of this comes free. McKinsey restructured partner compensation because outcome fees move with results instead of arriving on a predictable schedule, so a weak project now shows up in revenue, not just in utilization. Fixed fee and outcome pricing also still need a pipeline of engineers working toward the license that eventually lets them sign something themselves, and a firm cutting junior hours to fund an AI-driven margin gain is, at the same time, cutting the training budget for the next generation of people who can carry that signature. That is a real tradeoff to manage, on a normal planning cycle, not an argument against making the shift.

The firms converting AI into margin right now are not pricing the hours it saves. They are pricing the signature it still cannot legally get.

I will put a date on this. By the end of 2027, at least one more of the top global AEC firms, Arup, WSP, Jacobs, Stantec, or Mott MacDonald, will publish a specific percentage of fees moved to outcome or fixed-fee pricing, the way McKinsey just did. Confidence: medium, since AECOM's own numbers already point that direction and the underlying incentive is the same across the group.

What I am watching next is whether any state licensing board tests the ASCE position directly: a case where a firm leaned hard on AI output and the question of what the signing engineer actually reviewed becomes the substance of a claim. That is the event that would show whether the stamp holds as a durable line, or turns out to be as soft under real pressure as a taxi driver's knowledge of the streets.

---

<!--
Author note, delete before publishing:
- This replaces articles/2026-08-29-the-boat-is-gone.md, which you rejected as generic and
  dramatic (Gallup engagement stats, a purpose-crisis framing, an emotionally staged version of
  the same Iran anecdote). Same anecdote kept, cut down to two sentences and used once, purely
  as a mechanism illustration, not the emotional centerpiece. Delete the old file once you've
  confirmed this version is the one to run; I left it in place rather than deleting it myself.
- Reframed entirely around the newsletter's own ownable thesis, repricing judgment, using real
  2026 fee-structure moves instead of sentiment survey data. Core original claim: civil and
  structural engineering have a licensure-based legal floor under the part of the job AI cannot
  take (the PE stamp), which the taxi driver/GPS precedent never had, and real firms are already
  pricing around that gap.
- Pillar changed from talent to economics, since the throughline is about fee structure and
  margin mechanics, not organizational or purpose questions.
- Sourcing notes for the fact check pass:
  - ASCE Policy Statement 573 and the arXiv field study (2608.27364) were both read directly.
  - The McKinsey/BCG/Bain fee figures come from AI Weekly's reporting, which states its own
    original source as the Wall Street Journal; I did not reach the WSJ piece itself directly.
    The article itself flags the BCG and Bain percentages as self-reported at media events, not
    audited, which I carried into the piece as a calibration line.
  - The AECOM/Baird figures (20 basis points per 1 percent labor savings, margin targets through
    2029, time-and-materials pressure) were read directly from the Yahoo Finance piece. An
    earlier search result claimed AECOM acquired a firm called Consigli for $390 million; I could
    not verify that claim on a direct read and left it out entirely rather than risk an unsourced
    number.
  - The Autor and Thompson bookkeeper/taxi driver findings are from MIT Sloan's summary of their
    research, not the original paper, same caveat as in past issues that cite a secondary summary.
- No prediction logged yet; prediction_logged stays "no" until you publish and copy the dated
  prediction into templates/predictions-ledger.md.
- Run the pre-publish checklist in docs/style-guide.md, and read it aloud once, before this goes
  out.
-->
