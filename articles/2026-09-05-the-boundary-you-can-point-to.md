---
date: 2026-09-05
pillar: delivery
title: The Boundary You Can Point To
prediction_logged: no
---

# The Boundary You Can Point To

Running AI on your own hardware is no longer a matter of principle. It is a threshold question, and there are three tests. A firm needs only one of them to come back yes. Most firms are still arguing the principle, which is why the decision keeps stalling.

The first test is whether someone has already decided this for you.

Firms underweight this one, because it does not arrive looking like a technology decision. Roderick Bates wrote in February 2026 that project contracts increasingly restrict how AI tools may handle project information ([PBC Today, Roderick Bates](https://www.pbctoday.co.uk/news/digital-construction-news/construction-technology-news/2026-will-be-the-year-local-ai-emerges-in-aec/159253)). Where that is happening, the limit reaches a firm through its commercial team, well before IT hears about it. His piece carries no adoption figures, so I read it as a well placed observation, not as measured evidence.

Where no contract binds a firm, a regulation might, and those are sharper. Controlled Unclassified Information carries handling rules under 32 CFR Part 2002. A commercial AI tool that routes data through outside servers does not meet them. ITAR goes further. It restricts passing controlled technical data to foreign nationals. So there is an open question: if a provider's staff include non US nationals, does sending them that data count as an unlicensed export on its own? The Directorate of Defense Trade Controls has not ruled on it. Vendors in the space expect guidance within a year to eighteen months ([Sphere, AI for Defense Contractors](https://www.sphereinc.com/guides/ai-for-defense-contractors)). That estimate comes from a vendor guide, not from the regulator, so it is an industry expectation and nothing firmer.

The regulations themselves are not in doubt. A firm working on defense, nuclear, or some critical infrastructure has nothing to weigh here. The gate is shut. The only question left is what it builds inside the boundary.

The second test is volume, and the arithmetic is blunt.

Above roughly 2 million tokens a day, owned hardware wins. Below about 1 million, a hosted service stays cheaper ([Alpacked, self-hosted LLM guide, updated August 2026](https://alpacked.io/blog/self-hosted-llm-guide/)). A high end consumer GPU costs 3,500 to 4,000 dollars. Power adds about 65 dollars a month before anyone runs a single job on it.

Hardware is not the line that catches firms out. Paying someone who can actually run the stack usually costs more than the machines do. Pulling the other way, one deployment can serve several applications at once, which brings the crossover closer for a firm with more than one use for it. I am fairly confident in the shape of that curve. I am much less confident in any single dollar figure, since GPU street prices have been unstable and the source is a practitioner guide, not an audited study.

The third test used to end the conversation, and it is why the question is worth reopening now.

Open weight models, the ones a firm can run on its own machines, have closed most of the distance to the commercial frontier. A July 2026 comparison put one leading open weight model at 85 percent of a frontier model's composite intelligence score, and another at 95 percent ([Fastino, open-weight vs proprietary frontier models](https://fastino.ai/blog/closing-the-gap-open-weight-vs-proprietary-frontier-language-models)). Some of the coding benchmarks behind that comparison are vendor reported, which is a real caveat, and the gap still shows on hard multi step reasoning.

For summarizing a specification, checking a document set for inconsistencies, or drafting correspondence, a 5 to 15 percent difference in composite score is not what decides whether the output is usable. Reviewer time is.

![Three gates on running AI in house: whether a contract or regulation already fixes where data may go, whether throughput is past the roughly 2 million tokens a day crossover where owned hardware pays off, and whether open-weight models are good enough for the specific task. Each card carries what decides the gate and the catch that firms miss.](../assets/local-ai-gates.png)

Clear the gates and the payoff is about governance. It gets described loosely, so it is worth naming exactly.

A hosted service gives a firm a contractual commitment about how its data is handled. That is a promise. It is enforceable after the fact and it depends on the other party. A local deployment gives a firm a fact about its own architecture. The data did not leave, and that can be shown from the network itself instead of a vendor's policy page.

Those are two different kinds of assurance, and only one of them survives a client who asks to see it. That difference has started to matter commercially. In a survey of more than 1,000 technology decision makers across five countries, 42 percent named data security as the biggest barrier to AI adoption. Cost and complexity came second, at 33 percent ([Bluebeam, 2026 AI in Construction Report, via Lokalaise](https://lokalaise.de/en/blog/ai-in-construction-data-security)). That study was vendor commissioned and not peer reviewed, so I hold the exact split loosely and the ordering more firmly.

The risk is mostly about who maintains the thing.

A local deployment turns a subscription into an asset. Someone has to operate it, patch it, secure it, and eventually replace it. Model updates stop being automatic and become a decision. A firm that installs one and then understaffs it ends up with an aging model and a new attack surface, which is worse than what it replaced.

There is a quieter failure too. Buying hardware to meet a governance requirement that a well negotiated data processing agreement would have met, for a fraction of the effort. The first test catches that, as long as it gets asked before the purchase order and not after.

A data boundary you can point to on a rack is a control. A data boundary written into a vendor contract is a promise, and clients are starting to ask which one they are buying.

A date on this. By the end of 2027, the Directorate of Defense Trade Controls will have issued formal guidance on whether sending ITAR controlled technical data to a commercial AI service counts as an export. Confidence: medium. The question sits squarely in their remit and the industry has been asking it openly for over a year. Regulators also routinely take longer than the sector expects.

What I am watching next is one clause. Whether client contract templates start naming where AI inference must physically happen, and not only what a supplier may not do with the data afterward. The first is a requirement a firm either meets or does not. The second is wording. Once the first shows up in standard terms, running AI in house stops being a strategy discussion and becomes a bid qualification.

---

<!--
Author note, delete before publishing:
- New topic per your direction: local AI, benefits, cost of investment, data governance. Dropped
  the previous draft's subject entirely (articles/2026-08-29-ai-boost-ai-drag.md is untouched and
  still in place; tell me if you want it removed or kept as a future issue).
- Read "no pricing" as the newsletter's own repricing/billable-hour thesis, which you flagged as
  repetitive last time, not as a ban on cost figures, since you explicitly asked for cost of
  investment. So there is no fee-structure or billing-model argument anywhere in this piece, but
  the hardware and break-even numbers are in. Say the word if you meant it the other way and I
  will strip the dollar figures too.
- Pillar: delivery. This is the first issue in the archive to use it, per docs/content-pillars.md,
  so the quarterly rotation is now complete rather than economics-heavy.
- Dated 2026-09-05 (next Saturday) rather than 2026-08-29, since AI Boost, AI Drag already holds
  that date. Change the frontmatter and filename if you would rather run this one first.
- No headers, continuous prose, matching the format you responded best to on the last two issues.
  Structure is the three gates, which does the work headers would have done.
- Dropped the Iran anecdote. It was doing real work in the previous piece but the connection to
  this argument would have been forced, and this topic reads better leading straight with the claim.
- Sourcing notes for the fact check pass. This piece leans more heavily on vendor and practitioner
  sources than usual, because independent research on local deployment economics barely exists yet.
  I flagged each one in the text rather than hiding it, but it is worth your eye:
  - Bluebeam's 42/33 percent figures are vendor-commissioned research (July 2025, 1,000+
    respondents across five countries), reached via a secondary write-up, not Bluebeam directly.
  - The break-even and hardware figures come from a practitioner guide (Alpacked, updated August
    2026), not an audited study. Read directly.
  - The open-weight capability comparison (Fastino, July 2026) was read directly and itself notes
    that several underlying coding benchmarks are vendor-reported.
  - The ITAR and DDTC material comes from a vendor guide, read directly. The regulations cited
    (32 CFR Part 2002, ITAR foreign national restrictions) are real and verifiable independently;
    the 12 to 18 month guidance timeline is that vendor's expectation, which I labeled as such.
  - One claim I found in search results and deliberately left out: that the DoD Inspector General
    has opened investigations into contractors' unauthorized AI use, attributed to TechCrunch in
    February 2026. I could not verify it on a direct read and would not publish it unsourced.
  - Roderick Bates's piece was read directly. It offers no quantitative evidence, which I said in
    the text.
- No image generated yet, and no .docx. Tell me this draft is close and I will build both, same as
  last time. The graphic I have in mind is the three gates with their actual thresholds, so it
  carries the real numbers rather than illustrating the argument's shape.
- No prediction logged; prediction_logged stays "no" until you publish and copy the dated
  prediction into templates/predictions-ledger.md.
- Run the pre-publish checklist in docs/style-guide.md, and read it aloud once, before this goes out.
-->
