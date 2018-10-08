---
layout: default
title: "A Philosophy of Software Design by John Ousterhout [Talk]"
category: notes
---

# ["A Philosophy of Software Design" by John Ousterhout](https://youtu.be/bmSAYlu0NcY)

What is good software design?   
Can 10x programming be taught?    
Practice is the major component in being good   
Most profs aren't going to teach good design and coding; they don't have coding experience    

## Teaching Software Design Through Iteration (CS 190 at Stanford)
![philosphy_design_course_outline.PNG](/assets/philosphy_design_course_outline.PNG)
- 3 iterations
- Teams of 2
- Code is student reviewed and professor reviewed
- Students get (more effectively) exposed to design principles during code reviews 
    - Because they have practical examples of design failures
  
Fight Against Complexity 
## Design Concepts Taught
- Working code is not enough; must minimize complexity
- Classes should be deep
- Define errors out of existence i.e. make default behavior do the right thing
- Strategic vs tactical programming mindset
- and others:
    - complexity comes from dependencies and obscurity
    - general-purpose classes are deeper
    - new layer, new abstraction
    - comments should describe things that are not obvious from code
    - pull complexity downwards

## Classes Should Be Deep (or Modules, Functions, any layer really)
![philosphy_design_classes_should_deep.PNG](/assets/philosphy_design_classes_should_deep.PNG)
- Complexity cost of using the class: 
    - Learning the interface to the class
    - Understanding side effects
    - Adding dependencies

- Best case is simple interface, a lot of functionality
    - good abstraction, hiding complexity 

### Shallow Classes/Abstraction
- example:
    - reading serialized objects from a file means 3 classes: file stream, buffer and deserializer
- **Common case should be simple and not a series of shallow abstractions**:
    - if you must, use shallow classes for the edge cases
- not always possible to avoid shallow classes

### Deep Abstraction
- example: Unix file i/o with 5 functions open, close, read, write, lseek
    - hides dir management, permission checks, caching, path lookup, filesystem independence

### Goes Against Functions/Classes Should Be Small
- Priority is keeping abstractions deep

## Define Errors Out Of Existence i.e. eliminate exceptions as much as possible 
- In general, minimize exceptions
- **Try to to make the abstraction do the right thing in the common case**
    - e.g. don't throw an exception when unsetting a variable that has already been deleted [ this sounds like a declarative idea: 'ensure the state is the following'; should Unix not throw errors when deleting non-existent files? maybe it should not]
- Not doing the right thing in the common case creates a lot of complexity
- Testing still required and should uncover the right thing being the wrong this in a non-common case
- Crashing can be a good alternative to error handling extremely complex situations e.g. out of memory

[Overall disagree on this one, it seems this just leads to side effects as the "right behavior" is not always obvious, possibly hiding errors or states that should not be hidden within the contract of the abstraction. Maybe the idea is to build the abstraction to prevent this, or that clearly defines the right-behaviors but that's another thing entirely.]

## Mindset of Strategic vs Tactical Programming
Tactical programming:
- get next feature/bug done ASAP
- accept kludge, shortcuts
- technical debt accumulates in small increments, none of which seem particularly devastating at the time
    - however, cumulatively, it is 
- fixing becomes impossible: the debt is numerous little interlinked changes
- very easy to slide into this mindset

Tactical tornadoes: 
- programmers that output immense volume of shaky code but do so quickly
- leave destruction in their path
- business heroes: will deliver in short time

Strategic programming:
- Great design
- Develop fast in the future
- Minimize complexity
- Sweat the small stuff

### Tactical mindset pays off in short-term only

How much slower is tactical over how much time, how fast will strategic catch up? What time frame is short-term? Cannot say for sure but data-less opinion is 6-12 months. [conversely, a small (truly) throw-away project will benefit from a tactical mindset]  

### How Much to Invest?
- Continued small investments of 10-20%
- For new code:
    - careful design
    - documentation
    - testing
- Adding to existing codebase:
    - Because we can't get it right the first time:
        - improve something outside immediate fix/feature
        - goal is to eventually rewrite it through small changes

### Startup Pressure for Tactical Mindset
- Because of pressure to deliver 
- "Will clean up later", doesn't happen
    - Unless a complete rewrite occurs but it's rare

Facebook example:
- Incomprehensible/unstable codebase
- Can have terrible code and still business-succeed

Can also succeed with good engineering:
- Google, VMWare 
- Allows to attract better programmers
