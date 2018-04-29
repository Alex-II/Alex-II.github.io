---
layout: post
title:  "Testing Distributed Systems with Deterministic Simulation by Will Wilson [Talk]"
category: notes
---

# [Testing Distributed Systems with Deterministic Simulation by Will Wilson](https://www.youtube.com/watch?v=4fFDFbi3toc)  

([Slides](https://www.slideshare.net/FoundationDB/deterministic-simulation-testing))

Story of the FoundationDB group performing deterministic testing.

<u>Real-World: Clients and their Production Environments</u>  
Real-world has entropy that exposes (wrongly-believed) deterministic systems as non-deterministic because of non-deterministic events: race conditions, network issues, unexpected environmental events (e.g. power outage).  
These non-deterministic events make reproducing bugs hard to impossible.

<u> Simulator First </u>  
They wrote a simulator first, had no DB for years, debugging the simulator itself for years to make debugging the DB later possible and manageable. 

The simulator simulates all interactions between the DB software and the outside world: network access, disk access, system time, etc. It also simulates controlled failures of those outside-world interactions.


<u> Why The Simulator </u>  
The simulator allows for fully repeatable events to happen to the DB. Any failure or error that occurs in the DB is reproducible and explainable by the paramters of the simulator. Entropy in the outside world is only there if the simulator is asked to produce it.

<u>3 Ingredients of Deterministic Simulation</u>  
1. Single-threaded pseudo-concurrency: the simulator needs to simulate things that appear to happen simultaneously (network communication, disk access, other system calls) so it sounds like the simulator might enjoy use of parralelism. However, the simulator needs to not introduce non-deterministic events itself (which can happen too easily with parallelism) so it's got to run as a single thread of execution would.

2. Simulated implementation of all external communication: simulator needs to simulate and control external communication in order to control non-determinism; all entropy must be there because the simulator user decided to put it there.

3. Simulated processes need to be deterministic: the processes being simulated need to themselves be deterministic


<u>(1)Single-threaded pseudo-concurrency</u>  
They Couldn't write the simulator with many threads nor co-routines.
They used callbacks in C++ but callbacks are terrible in C++

They created a syntacic extension that 'compiles' down to C++: *Flow*.   
Flow allows the use of actor-model concurrency: entirely single-threaded implementation using callbacks.  

Example of Flow code:
```c++
ACTOR Future<float> asyncAdd(Future<float> f, float offset){  
    float value = wait (f); //waits for f to become ready  
    return value + offset;  
}
``` 
There's also a scheduler, single-threaded yet fast

<u>(2) Simulated implementations of all external communication</u>  
The DB integrated with the simulator via interfaces that the simulator satisfied.  
i.e. INetwork -> SimNetwork, IAsyncFile -> SimFile  

Simulated components are tunable   
e.g. simulated connections have simulated latency, simulated connections roll the dice on a read() call to determine success, failure, timeout, etc.

<u>(3) Simulated processes need to be deterministic</u>  
Programmers try to make the execution flow to fully and only depend on inputs (i.e. functional)   
e.g.  checking system time, checking disk space available can be non-deterministic if they're not received as input (DI-style)

<u>How to know if program is indeed written to behave deterministicallly?</u>  
They run some simulations twice with the same inputs. At the end, they check the app's random numbers generators to see if both are at the same step. Not foolproof, but helps.

<u>Test Files</u>  
Some test files, with configurable parameters, perform database operations.
They have constraints that should be met by the system and are verified at the end by the test.

Tests are brutal: links going down, network clogging, machines up, down, config changes on the fly.  
Tests can set machines in purposful degrades modes e.g. 10% of function calls fail.    
They also test their multi-paxos implementation.  
The simulate killing off datacenter, racks.  
They also simulate accidental human interventions: swap IP addresses, swap HDD.

The tests, using the simulator, are always deterministic, and can be reproduced.

<u>Tests vs Customers (Mis)using The Software</u>  
Customers will unearth all kind of weird bugs as they are exploring the input space and configuration space of the software, as they're using it in their particular environment with their particular software, hardware, needs and ideas.

How can testing discover the bugs before the customers?

1. Create more problems: In the testing world, disasters are made to happen more often than in the customer world, in hopes of encounterting a disaster before the customer. In testing, they speed up the DB's perceived time so that more events can occur in the system in the finite time time avaialble for testing.
2. Buggyfication: as a macro in testing mode, certain calls behave correctly (from an API contract perspective) but unexpecdetly. For example, sending data over the network  in non-normal ways to make sure contracts are respected between services: sending things out-of-(expected)-order, send things slower than expected, etc.
3. Hurst Exponent: essentially, failures aren't necessarily independent events e.g. causes of some failures are environment-dependent such that moisture that made one HDD fail probably shortened the lifespan of other HDDs in the rack. This idea is taken into account when testing and cascading failures are considered.

<u>Debugging</u>  
Due to use of callbacks, debugging is fairly broken but still possible.
It's mostly *Printf* which isn't that bad with deterministic behaviour.
The idea is that once it's fixed, it's fixed.

<u>Nightmare case: simulation is wrong</u>  
1) simulation is not brutal enough, not enough edge cases are imagined and not the simulator cannot convinciglty recreate such edge cases.
2) misunderstand contracts of OSes: simulation is only as good as our understanding of OS & hardware and assuming OS & hardware have no bugs themselves.

<u>Mitigation: the Sinkhole setup</u>  
Real, non-simulated, hardware setup: setup doesn't simulate OS & network, uses the real thing. Have networked controllable power supplies to turn machines on & off. 

Sinkhole setup found bugs in other things: a paxos library, a linux packet manager.

<u>Future directions</u>  
1. read team: test the simulation itself by introducing bugs on purpose and see if the simulation tests catches them.
2. more hardware: ??Unclear. I guess better hardware for the programmers??
3. try to catch bugs that elude the simulator: bugs that get through are bugs that the simulation doesn't catch. Programmers might tend to "learn" to write bugs that don't get caught by the simulation. Maybe have 2 simulation frameworks, one against which the programmers don't often test against.
4. more real-world testing: more sinkhole-like setups, more elaborate setups