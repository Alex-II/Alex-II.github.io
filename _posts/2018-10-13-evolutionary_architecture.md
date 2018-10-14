---
layout: default
title: "Building Evolutionary Architectures by Patrick Kua [Talk]"
category: notes
---

# ["Building Evolutionary Architectures" by  Patrick Kua](https://youtu.be/8bEsNT7jdC4)

## Change (Technical, Domain)  

### Technical Change  
- Programming languages
- Libraries
- Frameworks
- Tooling
- Operating environments (OSes, cloud environments)
- Technical constraints (dev machines)

### Domain Change  
- Revenue models e.g. subscription vs buying
    - importance of usage metrics, pricing data
- Base technology adoption
    - e.g. smartphone access (or not in certain countries)
- Competitors
- Customer needs
    - expectations have changed e.g. front-end 
- Markets
    - new domains e.g. 3D printing, cryptocurrency

## Case Study: Common Product Path 
1. Business idea
2. Architects determine requirements
    - what capabilities are needed for this business idea?
    - how do we get fast to market?
3. Architects start looking for third-party products to meet tech requirements
    - we use several third-party products so as to:
        - not be coupled to a particular vendor
        - to allow for change from the base implementation 
    - we plan for loose integration between our several products
    - we now need integration-products, needed when decoupling
4. Get a team to start:
    - start developing the product, work with third-party products
5. Takes lots of time to:
    - understand, define, integrate with third-party products
    - get vendor-specific customizations
6. Time passes, business has new ideas, wants product change
7. Third-party products need to be adjusted:
    - costly
    - slow (many months): third-party vendors have own schedule
8. integration bugs arise with recent changes
9. leads to prod environment being fragile because integration
10. leads to fear of changing anything because of the integration fragility
11. leads to change being hard, business is not happy


## Evolutionary Architecture   
Designing system for change instead of buying off the shelf and customizing later

<u>Evolutionary Architecture</u>: architecture that supports **incremental**, **guided** change as a first principle along **multiple dimensions**

## Incremental Change
Architectures are evolved through **incremental** releases:
    - Incremental releases represents **generations**  
    - **Generation**: architecture change due to business, technical change
    - **Time taken to get a simple change into production**
        - releasable, safe, stable, not cowboy ad-hoc results
        - i.e. continuous delivery, devops

<u> How fast is a generation? 6 months, 3 months, daily?</u>

### Rearchitecting 
Cycle:
    - Architecture phase: we try to make important decisions 
    - Development phase: we discover the problem space, and our false assumptions
    - Release phase: we discover more pains
    - Reflect phase: we prepare to change the architecture from lessons learned

## Guided Change
Evolutionary architectures are guided with fitness functions.

**Fitness function**: measure of how close a solution is to a goal

Must identify the attributes of the goal:
    - important attributes e.g. availability, mobile responsiveness
    - unimportant attributes e.g. localisation

Fitness function can be implemented through:
    - Metrics
    - Tests
    - Process

Fitness function type:
    - Atomic (unit-test style)
        - e.g. any cyclic dependencies, how much cyclomatic complexity, layer consistencies, checking dependencies
    - Holistic (system-wide)
        - e.g. performance tests that probe the as-close-as-possible-to-prod system; discovers config issues, side-effects
    - Continuous (not on a schedule or build trigger, constantly running)
        - e.g. Netflix simian army, like chaos monkey
  
## Dimensions of Change 
When making technical changes:
    - consider configuration
        - e.g. of a tool, how easy to manage? only GUI? 
    - consider upgrade
        - e.g. of a framework, do we test API changes? are they obvious? defer upgrade?
    - consider replacement/removal/swapping
        - e.g. of a library, how coupled is it?

### Domain Dimension of Change  
Business changes can be harder/easier, depending on architecture:
    - Big ball of mud architecture: 
        - ad-hoc whatever, spaghetti
        - change is hard, long, crazy coupling
    - Layered architecture:
        - tiers of separation e.g. DB - Repo - Service - Controller
            - e.g. Spring, Ruby on Rails
        - technical changes are easier
        - business rules can still be hard
            - business rule can affect all layers e.g. pricing rules
    - Microkernel architecture:
        - Core system with plug-in modules
            - core system has minimal business logic, specialized business logic is in the plug-ins
            - e.g. Maven, Eclipse, Firefox
        - Business & technical change are easy if domain matches the architecture
    - Microservices architecture:
        - per-feature/per-business need, independent layers of tech and business rules
        - tech easy to change: layers are independent, changes are local
        - domain easy to change: division is already per-feature
        - [extra infra work to link the microservices]

## Organization Structure
Older org model: per-tech teams 
    - front-end team, back-end team, DBA team

Better org model: per-feature teams
    - mixed-tech teams (front-end, infra, db, back-end), centered around business unit/need/feature

Inverse Conway Manoeuvre: shape your org to reflect the architecture that makes the most sense for the product

## Architecture Responsibility 
Be like a town planner, give directions of general development without approving every actual building construction.

<u>Decentralized governance</u>: Architects should help and educate other to make the right decisions, not make every decision for them

## Anti-Patterns and Traps
- The last 10% trap
    - last 10% takes a lot of effort, disproportionally so: tools and solutions might not properly work for it
- Coding via configuration
    - configuration becomes as complex as code e.g. test, source control, needs confidence
    - doesn't allow rapid changes
- Product customization (too much)
    - lock-in to third-party vendor schedule
- Exuberant coupling
    - not analyzing coupling & cohesion

## Build vs Buy
A spectrum of trade-offs:

![evolutionary_architecture_buy_build.png](/assets/evolutionary_architecture_buy_build.PNG)

