---
layout: default
title: "Your Brain on Software Development by Fahran Wallace [Talk]"
category: notes
---

# ["Your Brain on Software Development" by Fahran Wallace](https://youtu.be/t4z1Hmg5LC0)

## Cognitive Biases Affect Decisions
- Systematic errors in the brain's reasoning
- Evolutionary legacy parts for stress, predation, etc.

## Brain Model
- Brain stem: automatic responses (e.g. breathing, heart) 
- Limbic system: more complex stuff (e.g. emotions)
- Neocortex: Logic and thinking
- From *Thinking Fast and Slow*
    - Limbic & Stem: Fast (System 1)
    - Neocortex: Slow (System 2)


## Fast and Slow examples
*System 1, Fast*  
- 1+1
- Reading 'var x = 2;'
- Recalling feelings about a particular tech
- Keyboard shortcuts
*System 2, Slow*  
- Finding security bugs
- Database isolation level
- Drawing architecture diagram

## System 2 and System 1 interact
- System 1 has fast reactions or opinions to stimuli
    - what we see, hear, touch
    - recognize people, loved animals, flee from dangerous
- System 2 can override certain automatic decisions of System 1
- System 2 can train System 1 for different reactions, visual identification (looking for someone in a crowd)
- System 1 is like a hot cache of decisions
- System 2 can modify or add to the cache
- Nevertheless, System 1 is in charge by default

## Cognitive Biases in Software
### There's too much information:
- **anchoring effect**: attachment to the first idea 
    - e.g. writing mongodb as a placeholder will tend to make it permanent
    - e.g. hearing a guessed number from someone else will influence your own guess
- **availability heuristic**
    - i.e. when you're holding a hammer, everything is a nail
    - i.e. if something is in System 1 cache, you might use it
    - use C4 diagrams
    - write the constraints, name no tech or product
            
### Need to act fast:
- **hard-easy effect**: when a lot of pressure/rush, we do the easy things first
    - we feel there's progress when doing the fast easy things
    - research and planning is slow, feels like no process
    - ![brain_bias_value_difficulty_matrix.png](/assets/brain_bias_value_difficulty_matrix.png)
- **Dunning-Kruger effect**: confidence and knowledge about a topic are usually inversely proportional
    - despair when we turn unknown unknowns into known unknowns
    - ![brain_bias_dunning_kruger.png](/assets/brain_bias_dunning_kruger.png)     
### Not enough meaning:
- **Patterns Where There are None**
    - Correlation and causation mix-up
- **Cargo Cult**
- **IKEA Effect**: we're biaised towards things we've built 
- **Estimation of Time and Complexity**
    - we're really bad at it
    - we can't intuit the exponential complexity of tasks, how they interact and influence each other
    - simple tasks tend to have non-obvious edge cases
### What needs to be remembered?:
- **Peak-End Effect**: we remember emotional peaks (sad & happy) and the end of the project.
    - we forget the details, some lessons learned
    - use **Architectural Decision Register**: an immutable journal of decisions; gives the context behind decisions, explain, not repeat mistakes, not undo work, etc.

### Backfire Effect
- new concepts that contradict our held worldview offend our brain
- presenting facts will backfire: it won't convince the other person and instead might have them dig in deeper