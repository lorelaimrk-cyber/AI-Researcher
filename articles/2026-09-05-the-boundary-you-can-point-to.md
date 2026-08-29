---
date: 2026-09-05
pillar: delivery
title: The Boundary You Can Point To
prediction_logged: no
---

# The Boundary You Can Point To

Running AI on your own hardware stopped being an ideological position sometime in the last eighteen months and became a threshold question with three checkable gates. Most firms are still treating it as a philosophy debate, which is why the decision keeps stalling.

The gates are independent, and a firm only needs one of them to close to have its answer.

The first gate is whether something external already forces the boundary. This is the one most firms underweight, because it does not feel like a technology decision at all. Roderick Bates, writing in February 2026, made the point that project contracts themselves increasingly restrict how AI tools may process project information, which means the constraint arrives through the commercial team before IT ever sees it ([PBC Today, Roderick Bates](https://www.pbctoday.co.uk/news/digital-construction-news/construction-technology-news/2026-will-be-the-year-local-ai-emerges-in-aec/159253)). His argument is qualitative, with no adoption figures behind it, so I read it as a well placed observation rather than measured evidence.

Where the constraint is not contractual it can be statutory, and there it is much sharper. Controlled Unclassified Information carries handling requirements under 32 CFR Part 2002 that a general purpose commercial AI tool routing data through external servers does not satisfy. ITAR is stricter still: it restricts transfer of controlled technical data to foreign nationals, and the live question is whether sending that data to a provider whose infrastructure is accessible to non US staff is itself an unlicensed export. The Directorate of Defense Trade Controls has not issued formal guidance on that point, though vendors working in the space expect it inside roughly a year to eighteen months ([Sphere, AI for Defense Contractors](https://www.sphereinc.com/guides/ai-for-defense-contractors)). That source is a vendor guide, not the regulator itself, so the timeline is an industry expectation. The underlying regulations are not in doubt. A firm doing defense, nuclear, or certain critical infrastructure work does not get to weigh this against convenience. The gate is already closed and the only question is what it builds inside the boundary.

The second gate is volume, and this is where the arithmetic has become unsentimental. Current cost analysis puts the crossover for self hosting at roughly 2 million tokens a day, above which owned hardware wins, and below about 1 million a day, where a hosted API stays cheaper ([Alpacked, self-hosted LLM guide, updated August 2026](https://alpacked.io/blog/self-hosted-llm-guide/)). A single high end consumer GPU runs 3,500 to 4,000 dollars and draws enough power to add roughly 65 dollars a month before anyone touches it. The figure that catches firms out is not hardware at all. It is that the operational cost, meaning a person who can actually run the stack, routinely exceeds the hardware line, and that same analysis notes one deployment can serve several applications at once, which is what pulls the crossover forward for a firm with more than one use case. I am fairly confident in the shape of that curve and much less confident in any specific dollar figure, since GPU street pricing has been unstable and the source is a practitioner guide rather than an audited study.

The third gate used to be the one that ended the conversation, and it is the reason this is worth revisiting now. The capability gap between open weight models a firm can run itself and the proprietary frontier has narrowed to the point where it is no longer the binding constraint for most document and drafting work. One July 2026 comparison put a leading open weight model at 85 percent of a frontier model's composite intelligence score, and another at 95 percent ([Fastino, open-weight vs proprietary frontier models](https://fastino.ai/blog/closing-the-gap-open-weight-vs-proprietary-frontier-language-models)). Several of the underlying coding benchmarks in that comparison are vendor reported, which is a real caveat, and the gap does persist on hard multi step reasoning. For summarizing a specification, checking a document set for inconsistencies, or drafting correspondence, a 5 to 15 percent composite difference is not what determines whether the output is usable. Reviewer time is.

![Three gates on running AI in house: whether a contract or regulation already fixes where data may go, whether throughput is past the roughly 2 million tokens a day crossover where owned hardware pays off, and whether open-weight models are good enough for the specific task. Each card carries what decides the gate and the catch that firms miss.](../assets/local-ai-gates.png)

The benefit that follows from clearing these gates is a governance benefit, and it is worth naming precisely because it gets described too loosely. A hosted arrangement gives a firm a contractual commitment about how data is handled, which is a promise, enforceable after the fact, dependent on the counterparty. A local deployment gives it an architectural fact: the data did not leave, and the firm can demonstrate that from its own network topology instead of a vendor's policy page. Those are different kinds of assurance, and only the second one survives a client who asks to see it instead of being told about it. That distinction matters commercially, since data security now outranks cost as the reported barrier to AI adoption in this sector, cited by 42 percent of technology decision makers against 33 percent for cost and complexity, in a survey of more than 1,000 respondents across five countries ([Bluebeam, 2026 AI in Construction Report, via Lokalaise](https://lokalaise.de/en/blog/ai-in-construction-data-security)). That study was vendor commissioned and not peer reviewed, so I hold the precise split loosely and the ordering more firmly.

The risk case is straightforward and mostly about who maintains the thing. A local deployment converts a subscription into an asset the firm has to operate, patch, secure, and eventually replace, and it moves model updates from automatic to deliberate. A firm that installs one and then under staffs it ends up with an aging model and a new attack surface, which is worse than what it replaced. There is also a quieter failure: buying hardware to satisfy a governance requirement that a properly negotiated data processing agreement would have satisfied at a fraction of the effort. The first gate exists to catch exactly that, and it is worth checking honestly rather than as a justification written after the purchase order.

A data boundary you can point to on a rack is a control. A data boundary written into a vendor contract is a promise, and clients are starting to ask which one they are buying.

I will put a date on this. By the end of 2027, the Directorate of Defense Trade Controls will have issued formal guidance addressing whether transmitting ITAR controlled technical data to a commercial AI service constitutes an export. Confidence: medium. The question is squarely inside their remit and the industry has been asking it openly for over a year, though regulators routinely take longer than the sector expects.

What I am watching next is narrower and more useful as a signal: whether client side contract templates start specifying where AI inference must physically occur, rather than only what a supplier may not do with data. The first is an architectural requirement a firm either meets or does not. The second is a clause. Once the first starts appearing in standard terms, the local deployment question stops being a strategy discussion and becomes a bid qualification, and firms will discover which gate they were standing at all along.

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
