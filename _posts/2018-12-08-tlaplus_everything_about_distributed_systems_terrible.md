---
layout: default
title: "Everything about distributed systems is terrible by Hillel Wayne [Talk]"
category: notes
keywords: tla+, tla, distributed systems, verification
---

# ["Everything about distributed systems is terrible" by Hillel Wayne](https://youtu.be/tfnldxWlOhM)

## Distributed Systems
- Multiple Agents e.g. servers, machines
- Global Properties
    - system-wide (all agents) consistency, or safety property
- Localized Information
    - agents still have per-agent information, state, properties
- Partial Failure
    - some agents go down while global system still up
  
## Threads == Computers
Fundamentally, concurrent threads acting on shared memory is a lot like concurrent machines writing to a common DB.  

Minus partial failures for the threads + memory.

## Many Possible States for Concurrent, Non-Deterministic Agents
Without concurrency control, the combinations of states for agents interacting with shared data grows very fast.

For 2 agents, each doing this:

![everything_distributed_terrible_agent1_agent2.PNG](/assets/everything_distributed_terrible_agent1_agent2.PNG)  


Results in 13 states, 4 end-to-end behaviors 
(where an end-to-end behavior is a chain of states, starting at init, ending at one of the leaf states)

![everything_distributed_terrible_agent1_agent2_states.PNG](/assets/everything_distributed_terrible_agent1_agent2_states.PNG)  

For 2 agents, 4 steps each, we have about 550 states.

**The number of states and behaviors grows fast**

## Over a Long Enough Time, a System Will do Everything
Systems have:
- Undesired states: the system somehow has landed in a state that's bad
    - e.g. the state where all Kubernetes agents are unable to reach the Master
    - [e.g. deadlock? ]
- Undesired behavior: the individual states are fine but their chaining is undesired
    - e.g. a DB that never succeeds in converging
    - e.g. a consensus protocol that doesn't get consensus 

Eventually, invalid behaviors will occur.  
- e.g. a system processes messages: each message has 1 in 1 billion chances of going down the wrong behavior. Given 100 messages/second, we would expect to see the wrong behavior occur in 3 months, on average.

## Code With Concurrency Control/Abstractions Is Not Enough
Good to have semaphores, locks, promises, monads, etc.: they reduce the number of states the system be in.

However, these coding abstractions do not identify states, transitions and behaviors exhaustively and explicitly.
- i.e. does not help us understand bad behaviors or state, whether/how we reach them

## We Need Formal Specification
- Tool: TLA+   
- Model the system's behavior, possible states, transitions
- TLA+ finds undesired states [and behaviors?]
- Does not involve application code, only the imagined behavior
    - i.e. does not validate the code, validates the design
  
Second half of the talk is Hillel giving an example usage of TLA+.