---
layout: post
title:  "Serverless Computing: One Step Forward, Two Steps Back"
category: papers
---
# [Serverless Computing: One Step Forward, Two Steps Back](http://cidrdb.org/cidr2019/papers/p119-hellerstein-cidr19.pdf)

## Serverless: FaaS + Ecosystem
Serverless combines FaaS with a vendor's ecosystem for storage, caching, events, queuing, etc.


## The Good: Serverless' Autoscaling  
**Embarrassingly Parallel Functions**  
- Independent functions, performing map functions, need not sync or communicate between each other.  
- e.g. object recognition, image transformation, on-demand calculation

**Orchestration Functions**
- Use the serverless events to dispatch commands in another pipeline with its own separate autoscaling functionality 
- e.g. Google Cloud Dataprep by Trifacta

## FaaS Limitations
- Limited Lifetimes: most vendors limit a function to around 15 minutes
- I/O Bottleneck:
  - vendors provide little bandwidth (0.5Gb/s, 10x slower than an SSD)
  - AWS clusters a user's Lambda functions, increasing compute, reducing per-Lambda bandwidth
- Communication Through Slow Storage:
  - Lambda instances cannot communication with each other
  - They communicate by writing to another Amazon storage service
    - slow way to do IPC
- No Specialized Hardware
- FaaS instances are run in VMs separate from data they are processing

## FaaS Limitations Consequence
- Shipping Data to Code
  - we'd want to take advantage of caching, and other CPU and memory performance optimizations
    - maybe even keep a small internal state
  - data from everywhere is shipped to a short-lived function, where no optimization happens
    - as well as network, startup latency, bandwidth limitations
  - we'd like to see code shipped to live with data, processing it like a factory assembly line
-  Stymying Distributed Computing
   -  functions are not addressable (and can only communicate through slow storage)
   -  all need to read/write global state
   -  cannot use distributed systems to coordinate thousands/millions of FaaS functions
- FaaS stymies hardware-accelerated software innovation
  - vendors only offer no custom processing (e.g. GPGPU) nor large amounts of RAM for FaaS functions
- FaaS discourages Open Source service innovation
  - moss FOSS isn't made for FaaS integration
  - [we could imagine a User-Custom FaaS, where a spec dictates how User-provided software needs to run to integrate itself alongside the vendor FaaS infra]

## Case Study: Model Training
- Training ML model
- Needs 31 iterations

- On Lambda instance
  - cost 0.29$
  - total 465 minutes (7.75 hours)
  - each iteration:
    - 640 MB memory
    - 15 min (max allowed) 
    - 3.08 seconds
    - 2.49 seconds to fetch 100 MB
    - 0.59 seconds to process

- On m4.large EC2 instance
  - cost 0.04$
  - total 22 minutes
  - each iteration:
    - 0.14 seconds 
    - 0.04 seconds to fetch 100 MB
    - 0.1 seconds to process

- Lamba 21x slower, 7.3x more expensive

## Case Study: Low-Latency Prediction
- Using ML model for prediction
- Immediate downside: no GPU access in Lambda
- Batched inputs for prediction (AWS SQS)

- On Lambda
  - Fetch data from SQS, place results back in SQS
  - Average batch latency: 467ms
- On m5.large, still using SQS
  - Average batch latency: 13ms 
- On m5.large, using ZeroMQ instead of SQS
  - Average batch latency: 2.8ms

- Cost difference: order of 50x

## Case Study: Distributed Computing
- FaaS functions are not network addressable
- Communication happens through AWS storage
- Assessing cloud storage as communication medium
![serverless_one_step_forward_two_steps_back_distributed.PNG](/assets/serverless_one_step_forward_two_steps_back_distributed.PNG)

"Hence in the (unachievable) best-case scenario—when
each leader is elected immediately after it joins the system—the
system will spend 1.9% of its aggregate time simply in the leader
election protocol. Even if you think this is tolerable, note that using
DynamoDB as a fine-grained communication medium is incredibly
expensive: Supporting a cluster of 1,000 nodes costs at minimum
$450 per hour"

## As-Is Limitations May Be Good
- FaaS forces stateless
    - easy to write, debug, trivial to replicate  
- FaaS forces loosly-coupled design, possibly forcing good design patterns
- "In particular, FaaS limitations favor operational flexibility over developer control"
- May resurface ideas that fit the FaaS mindset    

## Paper Objections
Section 3.3 addresses some criticism and clarifications on the paper content.

## Improvements
- Fluid Code and Data Placement
    - infra needs to allow code and data to be colocated for perf reasons
    - infra might need to replicate data around to only couple data and code when needed 
    - high-level languages and frameworks can help the infra understand how to better move the data around
- Heterogeneous Hardware Support
    - offer access to diverse type of specialized hardware
    - allow infra to choose on which hardware to run the code for optimal execution
- Long-Running, Addressable Virtual Agents
    - infra should allow user to specify data or hardware affinity for code
        - e.g. infra would move data around, mode code and data to specific hardware 
    - amortize this effort by reusing code/data/hardware placement
        - needs addressable entities that are present long-term
- Flexible Programming, Common IR
    - different languages, DSL, frameworks may use an IR to accomodate infra-specific optimizations and constructs
        - e.g. data flow, hardware affinity, async events
- Service-level objectives & guarantees
    - offer granular SLOs, with penalties for mis-estimations
- Security concerns
    - security is aided by cloud provider
        - removing misconfiguration, mismanagment
        - offering high-level abstractions, allowing for security-benefial constraints
    - still need to consider multi-tenancy issues, leakage
        - especially if code is allowed to move fluidly as per user request
    - may need to adopt new tech (e.g. hardware enclave) and consider audit / post-hoc analysis