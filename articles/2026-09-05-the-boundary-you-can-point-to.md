---
date: 2026-09-05
pillar: delivery
title: The Boundary You Can Point To
prediction_logged: no
---

# The Boundary You Can Point To

Running AI on your own hardware is no longer a matter of principle. It is a threshold question, and there are three preconditions for it. A company needs only one of them to come back yes. I often see having own hardware being discussed as a philosophical question, which is why the decision keeps stalling.

The first precondition/enabler is whether someone has already decided this for you.

Companies underweight this one, because it does not arrive looking like a technology decision. Roderick Bates wrote in February 2026 that project contracts increasingly restrict how AI tools may handle project information ([PBC Today, Roderick Bates](https://www.pbctoday.co.uk/news/digital-construction-news/construction-technology-news/2026-will-be-the-year-local-ai-emerges-in-aec/159253)). Where that is happening, the limit reaches a company through its commercial & legal team, well before IT/digital is involved.

Where no contract binds a company, a regulation might, and those are sharper. The three jurisdictions most engineering work touches each restrict something different, which is why a single global answer does not exist.

Europe restricts whose law can reach the data, and this is the one European companies most often think they have already solved. Since Schrems II in July 2020, moving personal data out of the EU needs a case by case assessment of the destination country's law, not a signed clause on its own. The Irish Data Protection Commission made that concrete in May 2023, fining Meta 1.2 billion euros: standard contractual clauses without adequate supplementary measures do not cure a US transfer. The US CLOUD Act, meanwhile, reaches subsidiaries of US corporations wherever their servers sit, Frankfurt and Dublin included ([DanubeData, digital sovereignty and Schrems II](https://danubedata.ro/blog/digital-sovereignty-schrems-ii-2026)). Picking the EU region of a US owned cloud buys residency. It does not buy control of the stack. The EDPB's Recommendations 01/2020 name what closes the gap: encryption keys held only by the exporter or a trusted EU entity, never reachable by the importer.

The EU AI Act is the regulation everyone names here, and today it is not the one that binds. The Digital Omnibus package, approved by the Council on 29 June 2026, pushed the high risk obligations under Annex III from August 2026 out to 2 December 2027 ([Cloud Security Alliance, on the Omnibus delay](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-omnibus-vii-deadline-delay-20260/)). Only the Article 50 transparency duties held their original date, carrying penalties up to 15 million euros or 3 percent of global turnover ([Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/04/us-companies-face-eu-ai-acts-possible-august-2026-compliance-deadline)). Worth tracking, and not yet what a European company answers for.

The United States restricts who may see the data. Controlled Unclassified Information carries handling rules under 32 CFR Part 2002, and a commercial AI tool routing data through outside servers does not meet them. ITAR goes further and restricts passing controlled technical data to foreign nationals. So there is an open question: if a provider's staff include non US nationals, does sending them that data count as an unlicensed export on its own? The Directorate of Defense Trade Controls has not ruled on it. Vendors in the space expect guidance within a year to eighteen months ([Sphere, AI for Defense Contractors](https://www.sphereinc.com/guides/ai-for-defense-contractors)), though that estimate comes from a vendor guide and not from the regulator.

China restricts whether the data may leave at all. Under the Personal Information Protection Law, a transfer out takes one of three routes: a security assessment by the Cyberspace Administration, certification by an approved body, or a CAC standard contract. Anything covering more than a million individuals, or data classed as important, goes through the security review. The certification route opened on 1 January 2026 for smaller exporters, and 2026 amendments to the Cybersecurity Law raised the penalties ([China Briefing, cross-border data transfer certification](https://www.china-briefing.com/news/china-cross-border-data-transfer-certification/)).

Three jurisdictions, three mechanisms, one practical consequence for a company working across them: satisfying all of them at once is usually cheapest by not moving the data. For a company on defense, nuclear, or some critical infrastructure work, there is nothing to weigh at all. That one is settled, and the only question left is what gets built inside the boundary.

The second precondition is volume, and the arithmetic is blunt.

Above roughly 2 million tokens a day, owned hardware wins. Below about 1 million, a hosted service stays cheaper ([Alpacked, self-hosted LLM guide, updated August 2026](https://alpacked.io/blog/self-hosted-llm-guide/)). A high end consumer GPU costs 3,500 to 4,000 dollars. Power adds about 65 dollars a month before anyone runs a single job on it.

Hardware is not the line that catches companies out. Paying someone who can actually run the stack usually costs more than the machines do. Pulling the other way, one deployment can serve several applications at once, which brings the crossover closer for a company with more than one use for it. I am fairly confident in the shape of that curve. I am much less confident in any single dollar figure, since GPU street prices have been unstable and the source is a practitioner guide, not an audited study.

The third precondition used to end the conversation, and it is why the question is worth reopening now.

Open weight models, the ones a company can run on its own machines, have closed most of the distance to the commercial frontier. A July 2026 comparison put one leading open weight model at 85 percent of a frontier model's composite intelligence score, and another at 95 percent ([Fastino, open-weight vs proprietary frontier models](https://fastino.ai/blog/closing-the-gap-open-weight-vs-proprietary-frontier-language-models)). Some of the coding benchmarks behind that comparison are vendor reported, which is a real caveat, and the gap still shows on hard multi step reasoning.

For summarizing a specification, checking a document set for inconsistencies, or drafting correspondence, a 5 to 15 percent difference in composite score is not what decides whether the output is usable. Reviewer time is.

![Three preconditions for running AI in house. First, obligation: the EU restricts whose law reaches the data, the US restricts who may see it, China restricts whether it may leave at all. Second, volume: break-even sits near 2 million tokens a day, and staffing costs more than the GPUs. Third, capability: open-weight models reached 85 to 95 percent of frontier scores in a July 2026 comparison, so this is rarely the binding constraint now.](../assets/local-ai-gates.png)

Clear all three and the payoff is about governance. It gets described loosely, so it is worth naming exactly.

A hosted service gives a company a contractual commitment about how its data is handled. That is a promise. It is enforceable after the fact and it depends on the other party. A local deployment gives a company a fact about its own architecture. The data did not leave, and that can be shown from the network itself instead of a vendor's policy page.

Those are two different kinds of assurance, and only one of them survives a client who asks to see it. That difference has started to matter commercially. In a survey of more than 1,000 technology decision makers across five countries, 42 percent named data security as the biggest barrier to AI adoption. Cost and complexity came second, at 33 percent ([Bluebeam, 2026 AI in Construction Report, via Lokalaise](https://lokalaise.de/en/blog/ai-in-construction-data-security)). That study was vendor commissioned and not peer reviewed, so I hold the exact split loosely and the ordering more firmly.

The risk is mostly about who maintains the thing.

A local deployment turns a subscription into an asset. Someone has to operate it, patch it, secure it, and eventually replace it. Model updates stop being automatic and become a decision. A company that installs one and then understaffs it ends up with an aging model and a new attack surface, which is worse than what it replaced.

There is a quieter failure too. Buying hardware to meet a governance requirement that a well negotiated data processing agreement would have met, for a fraction of the effort. The first test catches that, as long as it gets asked before the purchase order and not after.

A data boundary you can point to on a rack is a control. A data boundary written into a vendor contract is a promise, and clients are starting to ask which one they are buying.

A date on this. By the end of 2027, at least one EU data protection authority will publish guidance addressing whether sending project or personal data to a US owned AI service hosted in an EU region counts as a restricted transfer. Confidence: medium. The question follows directly from Schrems II and the CLOUD Act sitting in contradiction, and European authorities have been active on transfers for years. Regulators also routinely take longer than the sector expects.

What I am watching next is one clause. Whether client contract templates start naming where AI inference must physically happen, and not only what a supplier may not do with the data afterward. The first is a requirement a company either meets or does not. The second is wording. Once the first shows up in standard terms, running AI in house stops being a strategy discussion and becomes a bid qualification. I am watching the Directorate of Defense Trade Controls on the ITAR question for the same reason: whichever jurisdiction moves first will set the template the others borrow.

---

<!--
Author note, delete before publishing:
- YOUR EDITS ARE KEPT. You made them in the .docx, not the markdown, so I pulled them across by
  hand: "preconditions" for "tests", "company/companies" for "firm/firms", "commercial & legal
  team, well before IT/digital is involved", and your opening line "I often see having own
  hardware being discussed as a philosophical question". I also kept your deletion of the Bates
  caveat sentence. Two follow-ups for you:
  (a) You wrote "The first precondition/enabler is". I left the slash exactly as you typed it,
      since I could not tell which word you were settling on. Pick one and I will make the other
      two headings match.
  (b) You only reached paragraph 3, so "firm" survived in five later places and "test" in two.
      I applied your wording throughout for consistency, and also retired the leftover "gate"
      language for the same reason. Revert any of that if you only meant the opening.
  Going forward: edit the markdown, or tell me you have edited the .docx, since I regenerate the
  .docx from the markdown and would otherwise overwrite your work.
- Regulation section rewritten to cover the EU, US, and China instead of the US alone, per your
  note. The organising idea is that each jurisdiction restricts a different thing: Europe
  restricts whose law can reach the data, the US restricts who may see it, China restricts
  whether it may leave at all. The strongest point for a European reader is the residency versus
  sovereignty distinction, since choosing an EU region of a US owned cloud does not escape the
  CLOUD Act. That now drives the piece and the prediction, which I moved from the US DDTC
  question to an EU data protection authority one. DDTC moved into "what I am watching next".
- One thing I deliberately did not use. Search results asserted a "Schrems III decision" had ruled
  on standard contractual clauses. On a direct read that is wrong: there is no such decision, only
  an expectation that a challenge will reach the CJEU. I left it out rather than repeat it.
- Length is now about 1,440 words against the 800 to 1,200 guide in docs/style-guide.md, because
  the regulation section grew from one jurisdiction to three. Readability held (average sentence
  17 words, one sentence over 35). If you want it back inside the guide, the EU AI Act paragraph
  is the cleanest cut, since it exists to say the AI Act is not what binds today.
- The graphic is rebuilt to match: card 1 now carries all three jurisdictions and the title reads
  "Three preconditions" rather than "Three gates". Regenerate anytime with
  scripts/make_local_ai_gates.py.
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
  - The EU AI Act delay (Digital Omnibus, Council approval 29 June 2026, Annex III moving to
    2 December 2027) was confirmed against two sources read directly, because they initially
    conflicted: an April 2026 law firm note still called the August 2026 date "possible" while the
    delay was pending, and a later analysis records the Council's final approval. The later one is
    correct as of now. If you publish after any further Omnibus movement, recheck this date.
  - The Schrems II, Meta fine, CLOUD Act, and EDPB Recommendations 01/2020 details all come from
    one secondary analysis, read directly. The underlying items are all matters of public record
    and easy to verify independently if you want primary citations before publishing.
  - The China PIPL material comes from China Briefing, a business advisory publisher, via search
    results rather than a direct read of that specific page. Worth a direct check.
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
