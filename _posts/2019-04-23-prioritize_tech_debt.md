---
layout: default
title: "A Crystal Ball to Prioritize Technical Debt by Adam Tornhill [Talk]"
category: notes
---

# ["A Crystal Ball to Prioritize Technical Debt" by Adam Tornhill](https://www.youtube.com/watch?v=SdUewLCHWvU)



## Information to Prioritize Tech Debt
- Where's the highest interest rate?
- Does the architecture support the way system evolves?
- Any bottlenecks for inter-team coordination?

## File Level Hotspots
- version control holds information on code changes through time
- tools can reveal info about files
- ![prioritize_tech_debt_hotspots_viz.png](/assets/prioritize_tech_debt_hotspots_viz.png) 
    - bigger circles: greater code complexity
    - darker circles: more frequent code change


## Prioritize Through Hotspots
- code change frequency much more important than code complexity metrics
    - complexity metrics are pretty bad, we can approximate to lines of code

- hotspots represent where code pays off to be clean, changeable, understandable, etc.
- in practice, hotspots usually are in bad shape, great refactoring candidates


![prioritize_tech_debt_distribution.png](/assets/prioritize_tech_debt_distribution.png) 

We can have:
- file-level hotspots
- function-level hotspots
- microservice/module/component level (by grouping related files)

## Supervise Trends
- ![prioritize_tech_debt_trends.png](/assets/prioritize_tech_debt_trends.png) 

## Normalization of Deviance
- as we accept situations that deviate from standards, we redefine the standards
- e.g. if we get used to a 6000 lines of code file, we tend to accept other large files, and increases in the 6000 lines of code file

## Temporal Coupling
- when a change occurs in A, a change in B quickly follows
- A and B are temporily coupled
- we should measure microservice temporal coupling

## Avoiding Microservice Shotgun Surgery Antipattern
- changing 1 thing means changing 5 services
- common reasons:
    - sharing code
    - leaky abstractions, depending on implementation
    - same team, several services
- we can use temporal coupling to detect this antipattern
    - this may indicate architecture needs to change

## Tools for Analysis
- Code MaaT
- CodeScene
- Evolution Radar
- Moose Platform

## Teamwork Implies Process Loss
- process loss: metaphor from mechanical inefficienies like friction and heat loss
- process loss cause:
    - coordination, communication overhead
    - diffusion of responsability

## Measure Team Coordination
- we can measure coordination hotspots
- ![prioritize_tech_debt_coordination_hotspot.png](/assets/prioritize_tech_debt_coordination_hotspot.png) 
    - shading indicates how many people from different teams work on that file/entity
- coordination overhead in such frequent multi-team changes
- worth investigating why such multi-team changes
- feature teams work if aligned with code being changed

## Resources
- book Your Code as a Crime Scene
- book Software Design X-Rays
- www.empear.com/blog
- codescene.io
