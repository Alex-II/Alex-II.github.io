---
layout: default
title: "The 7 Quests of Resilient Software Design by Uwe Friedrichsen [Talk]"
category: notes
---

# ["The 7 Quests of Resilient Software Design" by Uwe Friedrichsen](https://www.youtube.com/watch?v=v8hh0mB35wQ)

**Major challenges lies outside the code**

## Quest 1: Understading the business case
- Find a business case for resiliency 
    - what's the business value for the business?
- Business value:
    - is not about making money
    - it's about not losing money

Lack of resilience:
- reduced system availabiltiy
    - users annoyed with the system, go to competition
    - no transactions go through (e.g. ecommerce)
    - [erodes trust in the system in case B2B system]

## Quest 2: Embrace distributed systems
*"Everything fails, all the time"*

- Distributed systems are misunderstood
- We're taught to expect deterministic events
    - if X then Y
- In reality, events have probability of happening
    - if X maybe Y
- We sadly use deterministic thinking for non-deterministic systems
- Simple things in local systems become hard/impossible in distributed systems

### Failures in distributed systems
- crash failure: doens't respond
- omission failure: responds intermittently 
- timing failure: responds slowly
- response failure: wrong response (e.g. stale data)
- Byzantine failure: gone rogue

## Quest 3: Avoid the '100% available' trap
- Business or technical people might insist on 100% uptime
- No thought is given to behavior in failure modes

- **Failure will happen, when not if**

## Quest 4: Establish the ops-dev feedback loop
- In many places, ops and dev are still very separated
- In a distributed environment, infrastructure (ops) alone cannot provide good availability 
- However, non-determinism problems show up at the application level (dev)
    - Infrastrucutre (ops) cannot solve that
### Feedback loop:
- Ops notices problems in production
    - implies monitoring, metrics, observability
- Dev changes application-level to account for problems
- With a separation, communication takes a lot of time/not happening 

## Quest 5: Master functional design
**Without proper functional design, nothing else matters**

- Resilient software design means isolation:
    - isolate parts of the system from each other
    - to prevent failure cascade
    - to prevent system failing as a whole
    - bulkhead pattern
    - implementations: microservces, actors, SCS, etc

- However, system design is hard to implement correctly
    - no general solution: just because using microservices doesn't make system resilient, can still lead to cascading failures

## Quest 6: Know your toolbox
Many techniques exist:  
![7_quests_resilient_design_Toolbox.PNG](/assets/7_quests_resilient_design_Toolbox.PNG)

Resilience patterns:
- patterns are options, not obligations
- each pattern increases complexity
    - complexity erodes robustness
- each pattern costs money in dev, ops
- limited resilience budget
- choose complimentary patterns

Good systems only a handful:
![7_quests_resilient_design_Erlang.PNG](/assets/7_quests_resilient_design_Erlang.PNG)

![7_quests_resilient_design_Netflix.PNG](/assets/7_quests_resilient_design_Netflix.PNG)


## Quest 7: Preserve the collective memory
- Discussions seem to go back to basic ideas every few years (about 5 years says the presenter)
    - [This matches the idea that there's always a big influx of newcomers that aren't mentored so discover these not-new things and share these 'discoveries']
- We tend to discard old techniques because they're old
    - Wholeslae instead of selectively preserving the good stuff
