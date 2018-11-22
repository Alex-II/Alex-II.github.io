---
layout: default
title: "The Verification of a Distributed System by Caitie McCaffrey [Talk]"
category: notes
---

# ["The Verification of a Distributed System" by Caitie McCaffrey ](https://youtu.be/kDh5BrqiGhI)

<b> Great Notes, References (that should be read) from Presenter: https://github.com/CaitieM20/TheVerificationOfDistributedSystem </b>

## Formal Verification
- Safety: nothing bad will happen, system guarantees
- Liveness: something will eventually happen, there'll be progress
- A system tries to be both safe & lively 
- Highest degree of confidence

### Formal Specifications
- Read: <i>Specifying Systems</i> by Leslie Lampert
- Define properties of systems and verify we get the correct outcomes with these properties
- Amazon used TLA+ to verify infra, with success
    - increased confidence, found bugs
- Formal specifications are not code, code can still have mistakes
    - [Language details, implementation not respecting the specification, bugs in libraries, etc.]
- Does not eliminate need for testing
- Expensive to write

## Testing in the Wild
- Unit tests
- Integration tests
    - boundries between systems e.g. network boundries
- Types are not testing
    - Only as good as the type
    - [but so much better than non-types]
- Read: <i>Simple Testing Can Prevent Most Critical Failures</i>
    - Highlights:
        - [Paper should be read for a better understanding of these numbers]
        - 3 nodes or less can reproduce 98% of failures (integration tests)
        - untested error handling caused 58% catastrophic failure e.g. data loss, core system crash (unit tests)
        - 35% of catastrophic failures were caused by:
            - empty, log-only or comment-only error handling block
            - error handling terminates the cluster when non-catastrophic error handling could have been used

## Property-Based Testing
- Tests an input range in an unit-like test  
- QuickCheck, ScalaCheck, many other langueages
    
## Fault Injection
- Failure handling and confidence can only be tested when you force the system to fail
- Netflix Simian Army in giant scale
- Jespen-style testing for smaller scale
- Game Days:
    - Break production (shutdown rack, datacenter, network, etc)
    - Warn in advance, without too many details
    - Test software response 
    - Test people response e.g. communication, processes
    - Have team solely for observation
    - e.g. game day at Stripe with kill -9 

## Testing in Production
- Failure in production is high, but not a first step
- Monitoring is not testing, it's reactive
- Canaries
    - can only be compared to current-version while they're both running
    - usually verifies the happy path
    - e.g. if the canary is running and there's no partition, that never gest tested

## Research
Lineage-Driven Fault Injection:
- Records the happy path
- Injects errors that can affect the recorded happy path
- Tool <i> Molly </i> found bugs in Netflix, Kafka

