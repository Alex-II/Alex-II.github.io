---
layout: default
title: "Testing in Production, the safe way"
category: notes
---

# [Testing in Production, the safe way](https://medium.com/@copyconstruct/testing-in-production-the-safe-way-18ca102d0ef1)

[Author has a wealth of tools mentioned, papers to read and examples across the board]

## Testing in Staging 

Can't rely solely on staging. Testing **only** in a staging environment:  
- can give a false sense of security
- is rarely a good-enough approximation of prod 

### Staging Too Different From Prod
- can't test emergent behavior 
- size of staging cluster
    - can't address perf e.g. DB issues, GC pauses
    - several components running on the same machine removes network failures e.g. DB running on same machine as application
- small-scale behavior
        - small number of connections between components e.g. application and DB
- components usually fresh,
- infra components configured differently
    - e.g. DBs, load-balancer
- can't expose issues that occur over long term
    - .e.g. soak testing
- monitoring might not be deployed as well

Staging can't imitate production well enough.

## Testing in Production
Testing is prod is:
- not easy, not risk-free, not ad-hoc
- appropriate for services under direct, active control e.g. not embedded, not critical safety  

3 phases, as general concept

### Phase 1: Deploy
Deploy phase means:
- install a service on the prod infra
- do not direct any customer traffic to it yet

Deploy phase properties:
- is a near-zero risk phase
- *may* eliminate the staging environment altogether 
- requires sophisticated-enough infra e.g. Kubernetes, traffic routing of sorts
- deployed service can be tested against/alongside other prod services
- testing requests need to be distinguished from live requests

**Integration Testing**   
Still useful to:
- verify service contract is respected 
- verify SLO is attained 

A service(-under-test) will be receiving test-requests from testing framework.   
We're testing that service against prod components, to which it will itself make requests e.g. read/write from DB

Stateful components receiving requests from our service-under-test:  
- we don't want to affect used production data, create traffic bottlenecks
- even DB reads can muck up the DB cache

Strategies:
- DB knows it's a test-originating request:
    - mark changes in DB as test records [what about messing up the cache?]
    - use a different table for writes
        - still not quite the same as the real deal
- Service-under-test knows it's being tested:
    - discard a write to the DB at the last possible moment [so what about if it's read back?]

Strategies with Service Mesh:
- Sidecar proxy will have a canned response [maybe sidecar proxy can be a pseudo-fake?]
- sidecar proxies take care of marking requests as being tests
    - [the DB will need to know it's fake request]


**Shadowing, Dark Traffic Testing, Mirroring**  
Capture (or mirror) prod traffic, replay it against a deployed service.

Limitations: 
- Exact copy of real traffic might cause hiccups in stateful prod components e.g. service-under-test writes to the DB a record that exists already
- Best for idempotent requests, stubbing out stateful parts


**Tap Compare**   
Same as shadowing but compare the response from the existing prod services with the one from deployed service.

**Load Testing**   
Use a tool and appropriate monitoring to see how much the service can support.

**Config Tests**
- Configs are not obvious, hard to predict and cause for disasters.
- Should be tested as part of the deploy-testing procedures
    - to exercise code paths mediated by configs
- No config change should be cluster-wide, only incremental
- Good configs saved from rollbacks

### Phase 2: Release
Release (or rollout) phase means:
- service is handling customer traffic

Release phase properties:
- can be incremental aka. canary deployment [canary release]
- automatically incremented
- best when used with automated rollback, based on metrics & baselines
- rollback happens on hard failures:
    - crash loops
    - metrics threshold
    - invalid config

**Canarying**  
1. Promote part of the cluster to the new version.  
2. Observe metrics on the new population
3. Rollback if things go awry

[Canarying has its issues](http://dreynaud.fail/canaries-in-practice/)

**Monitoring**  
Challenge: identify which signals are important (3-10 signals)
Examples:
- increased error rate
- increase latency
- decreased requests being sent to the service

**Exception Tracking**  
Monitor requests that caused exceptions, helps in debugging.

**Traffic Shaping**  
Slowly divert more and more traffic to the canary services.

### Phase 3: Post-Release
Post-release means:
- release seems to be going well
- time for debugging/long-term monitoring
- ensuring performance is adequate, edge cases handled

**Feature Flagging or Dark Launch**  
- In-code enabling/disable based on a config/header
- Problem with too many flags left behind (as opposed to cleaned up after the feature is considered stable)

**A/B Testing**  
For tuning

**Logs/Events, Metrics and Tracing**  
The "three pillars of Observability"

**Profiling**  
- Instrumentation to measure performance
- Helpful to have good visualization/analysis

**Teeing**  
Like *Shadowing* but saving the traffic for debugging.

**Chaos Engineering**  
Willingly cause faults in the system to assess its reaction 

e.g. introduce latency, kill nodes, send fuzzed data

- Needs base stability







