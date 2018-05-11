---
layout: default
title: "My 10 Fears About the Future of the DBMS Field by Dr. Michael Stonebraker [Talk]"
category: notes
---

# [My 10 Fears About the Future of the DBMS Field by Dr. Michael Stonebraker](https://www.youtube.com/watch?v=DJFKl_5JTnA)

<u>Biggy Fear #1: Hollow Middle</u>  
DB interests in 1977, that he considers core:
- storage structures, query processing, security, integrity, query languages, data transformation, database design, data integration

Percentage of papers published in SIGMOD (top-tier publication) on these core issue reached low of ~50% in 2017 vs 100% in 1977.
Papers are being published in subjects in the 'application' level
This is normal, since understanding of the core has increased, so people migrate to outer layers.

DB field should be multi-furcating (creating offshoot specialisation  conferences): application-level spaces are so different from one another: people working in DBs for NLP might not be able to understand DB people working with complex analytics.

Time to multi-furcate officially! Time to make other conferences for these specialization.

Keep conferences for these core problems, other conferences for application-specific problems.


<u>Biggy Fear #2: We have been abandoned  by our "customer"</u>  
40 years ago, industry people came to SIGMOD conferences
- pathfinders from different industries (financial, insurance, oil & gas) looking for DBMS solutions to their
- keeping researchers connected to relevant problems

Today, no more industry people. Why? Conferences no longer relevant to them.
Only big players like Google, Amazon still show up; otherwise, it's a disconnected  echo chamber 

Dangerous to have lost touch with the problems-that-need-solving.

Big players: they have not-invented-here syndrome, they build in-house.
Big players are not very representative of the DB customer population, they're outliers.

<u>Biggy Fear #3: Diarrhea of Papers</u>  
In 1971, speaker got his PhD with 0 publications. In 1976, tenure from Berkeley with 5 publications.

Today, PhD needs 10 papers, tenure 40 papers.

To reach crazy numbers, people split their paper into *least publishable units*.
Students focus on "quickies", and incrementalism, with minimal implementation as it takes too much time to implement.

Postgres would be impossible today, too little papers for the implementation work.

Solution: top US university should cap the amount of papers RAs can list when applying RA to say 3 (smaller universities will follow).
If you can only submit 3 papers, you might make good 3 papers instead of 10 mediocre ones.

<u>Ancillary Fear #4: Reviewing is Getting Very Random (related to Hollow Middle and Paper Diarrhea)</u>  
Quality Stinks: Avalanche of papers being sent for review; in turn, huge program committees with many junior reviewers.
Lead to a revise and resubmit (to another conference) mentality
Destroying the reviewers, and submitters.

Solution: deal with hollow middle (specialise the papers) and paper diarrhea

<u>Ancillary Fear #5: Research Taste has Disappeared  (related to Customer  Leaving, Replaced by Big Players)</u>  
Big Players write papers, software. Research community doesn't review them critically enough.
Example: MapReduce, written by Google. 10 years later, Google accepts it wasn't the right way to solve the problem. They aren't using MapReduce anywhere anymore: they didn't understand DBMS when they wrote MapReduce. Why didn't the Research Community catch this? 

Big players pumps out bad ideas because they're inexperienced/unknowing and research community doesn't correct them.
Big players also pump out ideas for marketing reasons.

Research community needs to reconnect with real-world needs: make conferences more relevant, make it free for industry.

 
<u>Ancillary Fear #6: We are polishing a round ball (related to Diarrhea of Papers) </u>  
Convoluted papers with marginal increases in performance/features/qualities but immense increases in complexity.
One unrealistic solution: get RAs to work in industry for 1 year, to understand no one is going to implement complex stuff for marginal gains.

<u>Ancillary Fear #7: Irrelevant Theory is Taking Over (related to Diarrhea of Papers, Custom Abandonment) </u>  
Difficult to get (practical and useful) systems papers accepted in conferences:
- not enough theory, not enough generalization
- might cause divorce

When no longer driven by real world problems, arbitrary or theory-heavy papers get rewarded

Real world doesn't share data, proprietary data: system papers are becoming more artificial (artificial benchmarks, or edge case benchmarks)

<u>Ancillary Fear #8: We are ignoring the most important problems (related to  Diarrhea of Papers, Custom Abandonment) </u>  
We want to quickies so we solve problems that are easy to solve

Not working on:
- data integration (to alleviate data cleaning, ordering and finding, which takes 80%-90% of data scientists' time)
- database design and evolution (no one designs databases per textbook, why?)
- tuning DBMS is too difficult 
- average DBMS takes 20M$ to get into production readiness

DBMS field has lost its way as it forgot who the customer is.

<u>Big Deal Fear #9: Research Support is Disappearing (USA Perspective)</u>  
Too little gov investment, too little industry investment
Toast in the long run relative to other countries, unless aggressive investments are made.

Reminiscent of Roman Empire falling.

<u>Big Deal Fear #10: Student Loans (USA Perspective)</u>  
CS departments overrun with students:
- MIT has 40% undergraduates majoring in CS, faculty under load
- academic life becomes less attractive: best people will depart for greener and better paid pastures
- if big players hire the brightest out of academia, can't sustain research in academia


<u>Summary</u>  
Most fears are addressable:
- require hard decisions by people in power
- most important points: paper diarrhea and fragmentation



























