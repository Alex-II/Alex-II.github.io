---
layout: default
title: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure"
category: papers
---

# [Dapper, a Large-Scale Distributed Systems Tracing Infrastructure](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/36356.pdf)

## Google's Needs for Distributed System Tracing
Services have complex dependencies on other services, and a service's dependencies can dictate that service's overall performance (including dependencies of dependencies).

Looking for latency or performance issues is complicated:  
    - multitenancy creates intermittent problems   
    - dependencies may change, service internals not obvious

## Dapper: Ubiquitous Monitoring  
Monitoring needs to be ubiquitous because: 
- performance issues can occur in unexpected or edge  parts of the system
- because some issues cannot be easily reproduced

## Objectives  
- low overhead
    - marginal overhead so that there's no incentive to turn it off
    - small codebase ~2k LOC
    - uses sampling 
- application-level transparency
    - developers should not be aware of the system
    - need for continued developer care to maintain the system makes it fragile
- scalability      
- trace results quickly available  
    - faster reaction to production anomalies

## Instrumentation  
Trace, Span, Tree  
![dapper_span.PNG](/assets/dapper_span.PNG)  

- All Google services use common core libraries for:
    -  communication (RPC, async callbacks)
    -  threading, thread pools
- Dapper is integrated in this common core to trace inter-component communication and intra-component work
    - some applications still use Dapper-unsupported communication e.r. raw sockets, SOAP 
- Dapper allows developers to add annotations (textual, key-value pairs)
- Annotation sizes can be capped 

## Trace Collection       
Traces are written to disk, collected from hosts and stored in BigTable  
Collection is out-of-bound to not affect network in production    
Latency, from first logging to presence in Big Table:  
- Median: 15 seconds
- 98th percentile:
    - 75% of time, <2 minutes
    - 25% hours, hours

## Security  
- RPC/callback payloads are not automatically logged; opt-in only
- Dapper monitors communication endpoints for incorrect encryption, or unauthorized inter-component communication

## Tracing Overhead  
Runtime costs:
- span creation ~200 ns
- skipped annotation ~9 ns
- average annotation ~4 0ns

Measured overhead:  
![dapper_perf.PNG](/assets/dapper_perf.PNG)  

## Collection Overhead  
- Low CPU use < 1%
- Low network usage < 0.01%
- Average 426 bytes / span

## Sampling  
- sampling of 1/16 is barely measurable
- yet sampling of 1/1024 is enough data for meaningful data  
 
## Adaptive Sampling  
- sampling per unit of time, not per request volume
    - e.g. #traces/second instead of #traces/requests
- i.e. low traffic apps will increase the #traces/requests, high traffic will decrease #traces/request 
- an error in high-throughput services will occur thousands of times (and be caught by a trace)
- an error in low-throughput services will occur more rarely so more aggressive tracing is needed

## Uses
- Integration with exception handling
- Inferring dependencies
- API used for both tools and human inspection