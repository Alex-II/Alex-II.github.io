---
layout: default
title: "Microservices at Netflix Scale: Principles, Tradeoffs & Lessons Learned by Ruslan Meshenberg [Talk]"
category: notes
---

# ["Microservices at Netflix Scale: Principles, Tradeoffs & Lessons Learned" by Ruslan Meshenberg](https://youtu.be/57UK46qfBLY)

## Microservices: Benefits and Costs
Costs of microservices aren't popular discussion points

## Netflix Journey to Microservices
- A 7-year journey
- Triggered by need to move to Cloud
    - Made the move by moving small bits
- Monolith 4-day failure triggered the transition
  
### First Principles
Some assumptions/philosophy when beginning the transformation  

- Build vs Buy (including contributing to OSS)
    - Use, contribute to OSS
    - Build as last resort, when existing solutions don't work, can't be adapted
- Services should be stateless (except persistence/caching services)
    - not relying on sticky session, for example
    - any node can be hit with any request
    - verify this by chaos testing
- Prefer scale out rather than scale up
    - adding new instances is easier in the long run
    - hitting scale up limit is painful
- Redundancy, Isolation for Resiliency 
    - make more than one anything
    - isolate blast radius for a given failure
        - i.e. reduce the cascading effect of one system failing
- Automate destructive testing e.g. Chaos engineering, Simian Army
    - Failure will occur for sure
    - Detect failure early when everyone is at work, alert
    - [Reveals hidden, unpredicted failures]

### First Principles in Action, Lessons
- Automated destructive testing
    - really needed, nothing beats testing in production, dev & QA are insufficient
- Data: from RDBMS to Cassandra
    - Because Cassandra scales well
    - Allows for tunable consistency
        - can do things like having a satisfactory region-local quorum and replicating asynchronously between regions

### Netflix Optimization Priorities
![netflix_microservices_priorities.PNG](/assets/netflix_microservices_priorities.PNG)  
where innovation means feature velocity


### Microservices: Benefits
- Allows end-to-end ownership of microservices
    - one team does dev, testing, deployment, maintenance
    - motivation to make code reliable, deployable, testable
        - because they deal with the problems
    - hopefully, ownership also motivates to deliver impactful features
    - no blockers, delivery of features decoupled from waiting on other teams
    - [i.e. feature/vertical teams, devops]

### Microservices: Costs
Microservices are an organizational change  
- No more QA team, no more Ops team
        - people will get fired, emotional/morale affecting
- Centralized *infrastructure* investment [automating infrastructure resource management]
    - no longer centralized *roles* for gatekeeping (DBA managing DB things, storage people planning, budgeting, operating all storage)
    - e.g. devs use tools to request storage, DBs
    - need to build/buy/use tools to automate these once-centralized processes
    - need to build/buy/use tools observe, monitor, correct needs for capacity, budget
    - there can still be consulting e.g. DBAs can help a team define a schema but DBAs do not operate/deploy/maintain the DB
- transition period: Roman riding
    - transition takes times
    - in meantime, dual stacks, dual maintenance, same feature for each stack
    - replicate data 

### Microservices Lessons Learned
- IPC/RPC crucial for loose coupling
    - common contract/language between services
        - every service is communicated with in similar ways
    - consistency on ways application are deployed
- Caching to protect DBs
- Operational visibility 
    - how much information can be displayed per microservice with hundreds of microservices
    - how human intervention vs automation when problem appears
    - making signal out of many metrics (noise)
    - visualization tools become important
- Reliability Matters
    - failure = rate of change * scale
    - Cascading failures happen
        - not all services are critical e.g. rating system, recommendation system
        - allow for degraded state 
    - Destructive testing in prod