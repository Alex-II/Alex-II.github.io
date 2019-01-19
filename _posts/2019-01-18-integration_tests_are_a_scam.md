---
layout: default
title: "Integrated Tests Are A Scam by J.B. Rainsberger [Talk]"
category: notes
keywords: tests, integration
---

# ["Integrated Tests Are A Scam" by J.B. Rainsberger](https://blog.thecodewhisperer.com/permalink/integrated-tests-are-a-scam)

In retrospective, **what he calls integrated tests might be called end-to-end tests**

## What Are Integrated Tests [end-to-end tests]? 
A test whose failure is not easily explicable   
i.e. cannot simply identify what the problem occurred
i.e. failing test does not reveal the problem, only that there is a vaguely a problem somewhere

Includes end-to-end & system tests

Unit tests should be viewed as **isolated tests**

## Why Do We Write Integrated [End-to-End] Tests?
- Despite 100% isolated/unit tests, bugs can still arise
- We find bugs by manual testing, a client finds it, an integration test finds it
- Incentive to write more integration tests
  
## Tests and System Design
- **Isolated tests show the quality of the design**
- Hard to write isolated tests? Poor design
  - e.g. ton of painful boilerplate before each unit test might indicate too many dependencies
- Use isolated tests to find design problems
- More integrated tests and less isolated tests means less feedback on our design
  - i.e. more integrated tests encourage sloppy design
  - e.g. more coupling, no cohesiveness
  - e.g. changing Connect 4 to Connect 6 should be relatively trivial 

## Vicious Cycle of The Scam
1. We have unit tests
2. We find a bug despite all unit tests passing
   - this happened because of poor design
3. We write more integrated tests to cover for poor design
   - instead of correcting the design
4. We continue with sloppier design
   - more integrated tests means less pressure to correct the design
5. With sloppier design, we create more bugs
   - sloppy design leads to bugs by itself
   - harder to write the unit tests
6. We now have less time to write unit tests, and our design now pushes us to write integration tests
   - i.e. more bugs, and yet less unit tests
7. We're back at having unit tests and still finding bugs

## Explosion of Number of Integrated Tests [End-to-End Tests]
Integration tests grow combinatorically as the number of components/path per component grow:
- 3 components: A, B, C
- A has 3 code paths, B has 5 code paths, C has 7 code paths
- That's 3*5*7 (105) tests to get all path combination

- Covering all paths requires order of magnitudes more integrated tests that we can write
- Can't gauge how many paths we've covered (somewhere between 1% and 80% but exact number is generally unknown)

## Contract Testing
### Server
Establish the server contract: what must a server accept, what must a server return for a given request.  
- Describes behavior of server given requests + some server state.
  - e.g. RPC guarantees, how they work together
- Tests for validation, verification, establish behavior for dealing 0, 1, few, many and error.
- Use mocks, stubs to replace dependencies and set up scenarios (e.g. database content)

Establish the contract of the server, rigorously test the component with mocks, stubs.

### Client
1. Establish the client contract: when the client emits a certain request, how does it handle the responses?
  - (given responses conform the contract)
  - Tests for validation, verification of handling of responses
    - e.g. 0, 1, few, many, error
2. When the client is triggered by its own user, does it produce the correct request? [the client being someone else's server, how does this jive with the previous segment?]
- Use mocks, stubs to replace dependencies and set up scenarios (e.g. system time)

[It's probably possible to write good mocks, stubs because the contract has been very well defined and behaviors entirely fleshed out]

## Client Tests and Server Tests Meet
- Client tests whether *it asks the right questions* and *can it handle all the answers*
- Server tests that it *accept requests* and *generates the correct response*

![integration_tests_scam_contract_tests_diagram.PNG](/assets/integration_tests_scam_contract_tests_diagram.PNG)

- Client "ask right questions" tests must have a server "accept requests" counter part
  - e.g. given a client test get-list-of-clients (and it receives empty list from mock/stub), there should be a server test for which the get-list-of-clients request from test makes the server generate an empty list. 
  - i.e. the client's 'ask right question' which, during a test, gets a response from mocks/stubs becomes, in a server test, the server's 'accept requests'.  

- Server's tested 'generates correct response' in a server test becomes the 'handle answers' in a client test

[These are component tests then, with the added coordination of one component's test input being another component's asserted output]

## Better than Integrated [End-to-End] Tests
- Tests now only focus on a component at a time.  
- Testing 2 components is now about testing each component individually, using isolated/unit/component tests.
  - i.e. one component's test is independent of another's
- The test multiplication became test addition 3+5+7 not 3*5*7
- isolated unit/component tests are faster, smaller, easier to understand
- if contract/collaboration/component tests are hard to write, design needs rework 