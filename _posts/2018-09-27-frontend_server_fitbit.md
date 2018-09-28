---
layout: default
title: "A Frontend Server, Front to Back by Zach Tellman [Talk]"
category: notes
---

# ["A Frontend Server, Front to Back" by Zach Tellman](https://www.youtube.com/watch?v=_1rh_s1WmRA)

Story of a front-end server aka a gateway server, a routing server

**For Fitbit, needed because a monolith needed to be broken up [i.e. the way microservices need routing]**
![frontend_server_monolith_break.png](/assets/frontend_server_monolith_break.png)


## Fitbit Frontend Server Responsibilities
- Route traffic
- Validate traffic
- Shape traffic

## 4 Important Properties (in order of importance-ish)
- Transparent  
    - extensive, quality metrics
    - easy to reason about internal workings
- Stable
    - not crash 
    - robust to malicious requests
    - robust to high traffic (e.g. shed traffic)
- Fast
    - minimal overhead
    - predictable performance
    - mitigate slow backend
- Extensible
    - small, easy to understand, easy to change, adapt
    - yet change should make it hard to violate other 3 properties
    - i.e. "indicate how it's meant to be changed"


## System Design: Looking at the Extremes
Consider:  
    - What extremes should the system handle e.g. peak req/sec  
    - What should the system do when going above/under the extremes

## Frontend Uses Async: Issues
- Faster, more throughput 
- Less transparent
    - no immediately obvious stack traces
    - no easy-to-reason about single thread of execution
- Less extensible
    - callbacks everywhere, less obvious for newcomers to reason about

## Adding Transparency: State Machine & Passports
- **Possible code paths are represented on a FSM-like diagram**

![frontend_fsm_diagram.PNG](/assets/frontend_fsm_diagram.PNG)

- **Code stamps a passport-object that maps to the diagram**

![frontend_fsm_passport.PNG](/assets/frontend_fsm_passport.PNG)

## Requests in Queues and Handling: Latency, Throughput, Resource Usage
Somewhat conflicting possible optimizations:
    - resource usage
        - make sure no resource is idle, min resources 
    - latency per request
        - all requests get served immediately
    - throughput
        - volume but not necessarily low latency though

## Load Balancing Techniques
Goal:
    - Minimize latency
    - Distribute work
    - Deal with workers that are unpredictably slow  

- Round Robin:
    - simple, predictable
    - slow workers gets as many requests as fast workers
        - amplifies slowdowns
- Least In-Flight: 
    - keeps track of queued requests per worker
        - least busy gets next request
    - more complex, less transparent, more overhead
    - great: slow worker gets few requests
    - bad: fast worker can just mean rapid erroring out 
        - amplifies requests erroring out as all traffic is sent to erroring out worker
  
- Least In-Correct-Flight
    - also keep track of worker errors
    - don't entirely starve erroring servers

![frontend_rr_least_in_flight_perf.PNG](/assets/frontend_rr_least_in_flight_perf.PNG)


## Important Metrics
    "You improve what you measure"
    Or
    "Everything you ignore get worse"

1. p999 Overhead
    - introduced by frontend server e.g. GC, computing routing
2. request rate 
3. error rate

## Lessons Learned
- Articulate goals and prioritize
- Model extremes of the system, decide on behavior
- Choose metrics 