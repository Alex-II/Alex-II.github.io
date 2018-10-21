---
layout: default
title: "Chaos & Intuition Engineering at Netflix  by Casey Rosenthal [Talk]"
category: notes
---

# ["Chaos & Intuition Engineering at Netflix" by Casey Rosenthal ](https://youtu.be/Q4nniyAarbs)

## Control Plane at Netflix
- It's user administration, authentication, DRM negotiation (but not the streaming itself)
- Entirely in the cloud, in several regions

## Focus of Optimization: Performance, Fault Tolerance and Availability
- Less experienced team choose one at the detriment of the others
- More experienced team balances their choice

## Microservice Architecture
Great for feature velocity  
A microservice can often a dependency on another microservice which itself needs another, and so on  

## Emergence of Undesirable System-Level Behavior
Interaction of system's components can make the system behave poorly even if each component behaves reasonably in isolation.  

### Imagined Example of Positive Feedback Loop  
- User erroneously spams 'refresh' on a page
- Requests are buffered due to the network
- Requests all hit the same server at the same time
    - same server because they're coming from the same user
- Due to (erroneous) rate of requests, server fetches (possibly-stale) data from its cache instead of making network requests
    - Network access wouldn't keep up with the rate of (erroneous) requests
    - Business logic dictates stale data is better than no data e.g. recommended movies, favorites list
- Because requests are served from cache, CPU load goes down
- Scaling service notices there's less CPU load so kills a few servers
- Remaining servers have to deal with even more load
- In turn, more of the remaining servers fall back on fetching (possibly stale) data from cache
- At this point, more users are noticing stale data
- Some users will start refreshing, exacerbating the issue 


[Without more details, this scenario sounds a bit silly; sounds like the scaling service messed up or the cache-only policy messed up]  

## Chaos Monkey and Chaos Kong

### Chaos Monkey
Randomly turns off a prod server during employee working hours  
Server failure can be noticed during working hours  

### Chaos Kong
Randomly turns off servers for an entire regions

## Chaos Engineering ([Principles of Chaos](https://principlesofchaos.org/))

"Chaos Engineering is the discipline of experimenting on a distributed system in order to build confidence in the system's capability to withstand turbulent conditions in production"


- Build a hypothesis about steady-state behavior
- Vary real-world effects
- Experiment in production
    - this cannot be replaced by synthetic tests
- Automate experiments to run continuously
- Minimize blast radius

## Intuition Engineering
Idea that large complex systems need to be understood at some intuitive level  

### Example: Visualization Tool (Vizceral)
- Tool that displays incoming requests, their destination and latency  
- Takes advantage of human ability for visual pattern recognition  
- Gives an intuitive sense of normality


