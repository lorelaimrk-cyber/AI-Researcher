---
date: 2026-08-08
pillar: risk
title: The Four Year Gap
prediction_logged: no
---

# The Four Year Gap

What a 2018 forum in Slovenia taught me about calling something decades away, and why quantum computing is due the same test.

## The claim

In September 2018 I sat in a session on artificial intelligence at the Bled Strategic Forum, the annual conference the Slovenian government founded in 2006, held each September on the shore of Lake Bled, that brings government leaders, diplomats, academics, and media together to discuss global strategic issues ([Wikipedia, Bled Strategic Forum](https://en.wikipedia.org/wiki/Bled_Strategic_Forum)). The session sounded like science fiction to me. I remember thinking it would not happen in my lifetime. Four years later, on November 30, 2022, the whole world got ChatGPT ([OpenAI](https://openai.com/index/chatgpt/)). I had the same feeling a few months ago, listening to a podcast about quantum computing and the risk it poses to cryptography, and this time I did not wait to find out if my instinct was right again. Quantum computers are nowhere close to running a structural model better than a laptop today. The gap between sounding like science fiction and sounding normal keeps closing faster than engineers plan for, and the part of quantum computing that needs a firm's attention this year has nothing to do with speed. It is what quantum computing already means for the data an infrastructure firm is encrypting right now.

## What happened

The podcast episode was about Q-Day, the point at which a quantum computer becomes powerful enough to break the encryption the internet runs on. Google set an internal deadline for that risk on March 25, 2026: full post quantum protection across its own systems by 2029, framed explicitly around adversaries recording encrypted traffic today so they can decrypt it once a capable machine exists ([Google](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/)). The number behind that urgency traces to Google researcher Craig Gidney, who published a paper in May 2025 showing that a quantum computer with fewer than a million noisy qubits could factor a 2048 bit RSA key in under a week, a reduction of roughly twenty times from his own 2019 estimate of about 20 million qubits ([arXiv](https://arxiv.org/abs/2505.15917)). NIST finalized its first three post quantum encryption standards on August 13, 2024, FIPS 203, 204, and 205, and is urging organizations to start migrating now rather than wait for a fixed cutoff ([NIST](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards)).

That is the cryptography side, and it is close. The civil engineering side is much earlier and far less certain. A 2024 review of quantum computing in civil engineering identified real potential in three areas: optimization problems like construction scheduling and structural sizing, machine learning for structural health monitoring, and simulations like finite element analysis. The same review found that today's quantum hardware is still what researchers call NISQ, noisy and without error correction, and that solving problems at the scale of a real bridge or building may require millions of qubits and a fault tolerant machine that does not exist yet ([arXiv](https://arxiv.org/html/2402.14556v1)). I do not think that timeline is close. I am fairly confident it is not decades away either, for the same reason 2018 taught me not to trust my own instinct about what counts as far off.

## Why it matters to a firm like yours

An AEC firm's real assets sit on both ends of a computing problem. On the output side, quantum computing is a long run bet on whether some of the heaviest computation a firm already pays for (topology optimization, materials simulation, network routing) gets cheaper or simply more thorough once the hardware matures. On the input side, the encrypted project data a firm holds today (geotechnical surveys, structural models, decades of proprietary IP, infrastructure control systems with long service lives) is already exposed to what security researchers call harvest now, decrypt later. An adversary records the encrypted traffic today and waits for a quantum computer capable of unlocking it later. That exposure begins the moment a capable quantum computer exists, which several serious estimates now place inside the working life of a project delivered today, long before quantum hardware becomes useful for the engineering work itself. The same leadership team deciding this year's AI tooling budget is, with far less fanfare, the one that will decide how much attention a cryptography migration gets before a client or an insurer forces the question.

## The benefit case

Start with what quantum computing has already been tested against in the field. Volkswagen ran the most public pilot relevant to civil infrastructure: during Web Summit in Lisbon in November 2019, nine public buses run by the transit operator Carris used a routing system built on a D-Wave quantum computer to calculate near real time paths through city traffic, following an earlier demonstration of congestion free route optimization for taxis in Beijing in 2016 ([Volkswagen Group](https://www.volkswagen-group.com/en/press-releases/volkswagen-optimizes-traffic-flow-with-quantum-computers-16995)). That is traffic and network design, a core civil and urban planning problem, tested outside a lab rather than only inside one.

Structural engineering has its own early research, and unlike most quantum computing papers today, this one reports a real head to head result. Researchers Zisheng Ye, Xiaoping Qian, and Wenxiao Pan split a classic structural optimization problem, finding the layout of material in a structure that minimizes how much it flexes under load, into a part solved on a normal computer and a smaller part solved on a D-Wave quantum annealer. The authors report, in their own abstract, that the hybrid method matched or outperformed standard classical heuristic methods on both solution quality and computational efficiency on the test problems they ran ([arXiv, Ye, Qian, and Pan](https://arxiv.org/abs/2301.11531)). I take that as a narrow, self-reported result on problems sized for a NISQ era machine. It supports a smaller claim than "quantum beats classical software on a real building": that a real structural design problem can be mapped onto quantum hardware and produce a usable answer at all, which is the harder problem to clear first. It is the first honest head to head data point I have found in this research, rather than another simulation of what might happen someday.

Materials science may be the case with the clearest payoff if it holds up. Quantinuum's researchers have used quantum simulation to model how metal organic frameworks, a class of materials being actively researched for carbon capture, bind carbon dioxide molecules, the same kind of chemistry that matters for capturing emissions at the point they are produced ([Quantinuum](https://www.quantinuum.com/blog/on-the-arxiv-modeling-carbon-capture-with-quantum-computing)). Cement alone accounts for around 8 percent of global CO2 emissions, and the calcination process itself releases carbon dioxide as a matter of chemistry, on top of whatever the kiln burns for fuel ([Chatham House](https://www.chathamhouse.org/2018/06/making-concrete-change-innovation-low-carbon-cement-and-concrete)). A materials scientist who can simulate binding energies accurately can start designing better sorbents with a modest quantum computer, well short of the fault tolerant machine that breaking encryption would require.

## The risk case

The honest risk sits opposite the benefit case in both certainty and timing. Every computational benefit above is still a proof that quantum hardware can be mapped onto a real engineering problem. Beating classical software at the scale a real bridge or building needs is a separate, larger claim the evidence does not support yet, and the estimates for when that changes keep moving. The cryptography risk depends on hardware that Google's own security team is now planning around arriving by 2029, three years from now, and breaking encryption only needs a quantum computer that is good at factoring large numbers, a far narrower machine than the one civil engineering would need ([Google](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/)).

I hold what follows loosely, because no one, including the people building the hardware, has a confident date. But I am fairly confident the ordering matters more than the exact year: an infrastructure firm's monitoring networks, control systems, and archives of structural and geotechnical data are accumulating encrypted exposure today, years before quantum hardware for engineering computation is likely to be worth a firm's time. A firm that waits for quantum computing to become obviously useful before thinking about it at all will, by that same wait, also delay thinking about the part of this that is already a live risk. The counter case deserves a fair hearing. Most AEC firms are neither defense contractors nor banks, and the migration deadlines set so far target national security systems and federal agencies only, so treating this as an emergency ahead of any actual requirement risks spending real budget on a threat that is, for a mid sized structural firm, still fairly abstract. That is a reasonable position, and a different one from ignoring the question until a client or an insurer asks it first.

## The throughline

> The distance between something sounding like science fiction and something being normal keeps getting shorter, and the safest place to stand is tracking a new technology's risk case years before its benefit case is ready to use.

## A prediction

> Prediction (2026-08-08): By December 31, 2027, at least one firm from the top 20 global AEC firms by revenue (a group that includes Arup, AECOM, Jacobs, WSP, Stantec, Mott MacDonald, and Ramboll) will have publicly disclosed a post quantum cryptography migration plan or timeline for its own systems, distinct from a general AI or cybersecurity statement. Confidence: medium.

## What I am watching next

Two signals, on two different clocks. On the near clock, whether any AEC firm follows Google's lead and puts a specific post quantum migration date on the record, rather than folding it into a general cybersecurity paragraph, since that detail would tell me a firm has actually mapped its own exposure rather than noted the trend. On the far clock, whether results like Ye, Qian, and Pan's start showing up on structural problems closer to the scale a real project needs, rather than the small test cases quantum hardware can currently handle, since that is the signal that would tell me the multi year timeline I am assuming is starting to compress the way the AI timeline did after 2018.

---

<!--
Author note, delete before publishing:
- This draft has already been through prompts/04 (style/fact pass) and an independent
  prompts/06 review (fresh Sonnet subagent, no context from drafting). That review's five
  antithesis-construction flags and the benefit/risk contradiction it caught have all been
  fixed in this version. One finding from that review is a genuine editorial call, not a copy
  fix, and is still open:

  ON THESIS: the reviewer read this as a real drift from the newsletter's core positioning
  ("AI is repricing engineering judgment"), not a marginal one. Quantum computing is a
  different technology from AI, and this piece does not touch the billable hour, staffing
  pyramid, or fee structure the newsletter is built around. I've tagged it pillar "risk" (data
  security exposure is the closer fit than "delivery") and added one bridging line in "Why it
  matters to a firm like yours" tying it to budget and leadership attention rather than forcing
  the AI repricing angle where the evidence does not support it. Whether that is enough, or
  whether this should ship as a deliberate one-off exception to the newsletter's usual
  boundary, given you asked for this topic specifically this week, is your call.
- This issue intentionally opens with narrative before the claim, at your direction, which
  bends voice rule 1 ("first two sentences state the claim, no warm-up"). The thesis lands by
  the end of the opening paragraph rather than in sentence one or two. The Bled/podcast anecdote
  doubles as the required "one human detail only the author could add," so no
  [YOUR DETAIL HERE] placeholder is used this issue.
- Runs about 1,500 words, above the usual 800 to 1,200 house range, given the personal opening
  plus three case studies. Trim a case (materials science is the most cuttable) if you want the
  tighter range instead.
- The Ye, Qian, and Pan arXiv paper (2301.11531) claim is now explicitly attributed as
  "the authors report, in their own abstract" rather than presented as independently verified.
  I could not get a full read of their methodology/results section (paywalled rendering issues
  on my end); the abstract itself is directly quoted and accurate. No institutional affiliation
  is listed on the arXiv page, so none is claimed.
- prediction_logged is correctly "no": per templates/predictions-ledger.md's own instructions,
  predictions get copied into the ledger the day an issue publishes, not at draft time. This
  matches how every other issue in this repo has shipped. The prediction wording itself is a
  starting draft, sharpen or replace it before it goes out.
- Run the pre-publish checklist in docs/style-guide.md yourself before shipping, and do the
  read-aloud pass; that is the one check nothing else in this pipeline can do for you.
-->
