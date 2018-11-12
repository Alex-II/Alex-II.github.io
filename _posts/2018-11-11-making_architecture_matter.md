---
layout: default
title: "Making Architecture Matter by Martin Fowler [Talk]"
category: notes
---

# ["Making Architecture Matter" by Martin Fowler](https://youtu.be/DngAZyWMGR0)

## Architecture [as an Ivory Tower]
- [Ivory tower] architects are: "some senior person in an organization who is setting rules and standards to how software should be written but hasn't actually written any software for maybe 10 or 20 years. And these architects [...] often cause a lot of problems for software projects [...]"
- Wrongful belief that architecture is beyond programming, architects shouldn't be programming

## What is Architecture?
- Hard to define without relying vague words like 'important components', 'important relationships'
    - How do we find importance?

- Architecture might be combination of two things:
    1. decisions that are hard to change 
        - i.e. from 'the decisions you wish you got right early because they're hard to change later'
        - e.g. programming language
    2. expert developers' shared understanding of system design
        - common understanding on how to the system works
        - implies a vague human-shared understanding
        - need a good shared understanding for growth
- Architecture of a system is what's important in a system.
    - [implies there needs to be categorization and description of priorities]
    

## Why Care About Architecture?
- Decisions on botching architecture is economic
    - Less architecture consideration means shipping next feature faster
    - "We need to put less effort on quality so we can build more features for our next release"
- Response shouldn't be "we need to be good engineers"
- Response should be rooted in economics
    - A good architecture will allow us to ship features faster; a bad architecture is only a short-term gain
    - Bad architecture will slow down adding features
    - Time when good architecture pays off is weeks, not months

![making_architecture_matter_stamina.PNG](/assets/making_architecture_matter_stamina.PNG)  
