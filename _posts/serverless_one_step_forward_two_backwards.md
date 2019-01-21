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

