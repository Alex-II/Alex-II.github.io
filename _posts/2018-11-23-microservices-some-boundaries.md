

# [DDD & Microservices: At Last, Some Boundaries!](https://youtu.be/yPvef9R3k-M)

## Microservices (as described by Netflix) Coincide Well with DDD
- Autonomous teams with isolated implementations
    - e.g. no shared DB with mixed domain models

## Adapters (Anti-Corruption Layer)
- Communication (patterns, objects) received from external components carries a certain model with it, which might differ from our internal component's model
- Adapters transform that implicit model that was received when receiving messages into the internal domain model.
- It allows for a the internal model to be precise, simple (or simpler), clearer, possibly more performant 
- The adapter is like a car filter, oil filter for an engine (high-precision component): filters providing the engine controlled air and oil because the non-filtered air and oil doesn't work well with the engine
-  Some components don't need filters (low-precision components), and they can work in degraded state with dirty conditions, and there isn't much trouble about it
- Let's assume we're dealing with high-precision components


## Models and Conformity Across Teams
- Assuming each team handles one microservice
- Microservices have an internal model and a communication model
- Often, the communication model reflects the internal model
- When sending/receiving data between microservice A and microservice B, Team A and Team B need to establish communication patterns and contents. This is human group dynamic, including organisational politics. The teams need to have some form of relationship:
    - Team A can establish a common model with Team B: they exchange data on a very similar business domain and they agree on a model that suits both. Both microservices share this common model and communication is easier for both.
    - Team A dictates the model and Team B fully conforms: Team B will change their service's model to accommodate communication with Team A; it's an asymmetrical relationship. Team A doesn't change their model at all. This can happen regardless of whether Team B is a client or server with respect to Team A.
    - Team A dictates the model and Team B uses an adapter: messages from Team B has an internal model different from Team A and uses an adapter to translate messages to and from Team A's microservice.
- Team C might fully conform to both A and B, because A and B are sending, business domain-wise, different information. Team C's domain model is therefore a bit of A and a bit of B.
 
## Models Need to be Clear, Not Big
- Gigantic models that cover every team, module, component, use case don't seem to be as clear or crisp
- Useful models need definitions which require context
- Useful models need simple assertions which require boundaries 
    - assertions (this always happens, this is always true) simplify interpretation of situations
    - global assertions are hard/impossible; the assertion can be true within a subset of global

## Issues with Shared Models
- If Team B conforms fully to Team A (without an adapter), any bad model decisions taken on by Team A will negatively affect Team B (and any other Teams that conform to Team A) 
- Even when, once more, Team B conforms to Team A, it's possible that Team B does not deliver the model as promised (i.e. the microservice B does not fully implement the intention of Team B). Team A will corrupt their own model if they don't use an adapter until Team B fixes their problem. 

## Have a Communication-Only Model
- If there is one dominant team (e.g. Team A) that everyone conforms to, this makes Team A the de facto global model of the system. 
- Even if teams build adapters, allowing them to have their internal model differ from the communication model, this still makes Team A the de facto communication model.
- If we're going have a global communication model, let's consider building an purpose-designed communication model that everyone conforms to, with out without adapters.

## Are Microservices Needed for Any of This Decoupling?
- In theory, these separations can be achieved without microservices, using logical boundaries
- In practice, only microservices offer incentive to not break them
    - Without microservices, it's too tempting and too easy to poke across the boundaries, make quick and dirty changes 
        - Accessing the DB when not supposed to
    - With microservices, the whole setup makes it less likely, more obstacles to cross the isolation
        - Accessing the DB of another microservice becomes way more complicated now
