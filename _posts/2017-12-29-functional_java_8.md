---
layout: default
title: "Core Design Principles for Software Developers by Venkat Subramaniam [Talk]"
category: notes
---

# [Core Design Principles for Software Developers by Venkat Subramaniam](https://www.youtube.com/watch?v=llGgO74uXMI)

## Good Design
A good design is a design that's easy to change

Correct solution takes iterations, constantly in evolution

Writing code first time is an exploration: many relationships are discovered, questions asked and answered.

When we're done, we should (utopically) delete it and rewrite it; rewriting will be much faster and we will rewrite with many lessons learned from first attempt.


## Quality of Design
Some ego is important: motivation, pride

Too much ego: can't let go of our bad designs

Care about solving the problem, not a specific implementation

Poor engineer: no initiative in changing the design

Code review and discussion: learn from others, teach to others

## Keep It Simple
Simple code communicates what it does clearly without exposing confusing/surprising details

Simple code solves a well-defined problem

Do not confuse simple with familiar.
Familiar means we're used to it, so it's easy for us, but it doesn't mean it's simple.

## Complexity 
Inherent complexity: comes from the problem domain\
Accidental complexity: comes from our implementation, e.g. deciding to use multi-threading 

Might be familiar with multi-threading so it's easy for us, but it's still not simple.

Determine if inherent or accidental complexity.

Good design: hides inherent complexity, eliminates accidental complexity 

## YAGNIyet

Implement things *later rather than now*, if:

	* it's equal or less expensive to implement it later
	* we're not sure if we'll need it later
	* (Thoughts: and if it can *actually* be postponed )

Why implement later?

	* we might learn more about the domain/vision/design of the thing we're implementing  e.g. we might figure out what DB features we need as the requirements clarify so we implement prod DB at the end
	* we might turn out to not need that thing
	* (Thoughts: we might do some other high-ROI activity instead)

Postpone != procrastinate (procrastination is not getting things done that should have been done)

Don't finalize one component at a time when several components interconnect.\
Work on several at a time and integrate them as they go along

**Postpone until last responsible moment**

### Why we don't postpone?
Because we're scared that we won't have time for testing. 

We take decisions early to test them and we're stuck with them.

With good testing, we can postpone certain decisions of implementations.

## Cohesion
Focused single responsibility\
Like things together, unlike things stay apart.
(Thoughts: makes code more readable, easier to reason about)

Allows per-responsibility code to only change when that responsibility needs to change.\
Instead of changing often because of many responsibilities\
(Thoughts: or worse many pieces of code change because they share the responsibility among each other)

Changing code is expensive, we want to affect the least amount of code when we introduce a change in the system.

## Coupling
More dependencies, more coupling \
Inheritance is a form of dependency 

Eliminate coupling when possible\
Make loose coupling otherwise

Depending on a class, tight coupling\
Depending on an interface, looser coupling

(Thoughts: coupling is how many secondary changes are required after a primary change. If changing one class means changing all the classes in some fashion, not cool)

## High Cohesion and Low Coupling
We want this!

## Dealing with Coupling
Reduce coupling by using interfaces

## Keep It DRY
Don't duplicate code itself\
Don't duplicate effort: similar subsets of code in different places but doing the same thing

Every piece of knowledge in a system needs to have a single authoritative representation\
(Thoughts: Domain Driven Design-style)

Refactor when you notice duplication

Use tools to find duplication

Don't hastily add abstractions before signs of duplication - remember YAGNYet

## Focus on Single Responsibility
Be able to describe the primary responsibility of a class, method, component without "and"s

### Long Methods
hard to test: permutation of input, output, states\
hard to read\
hard to remember\
hard to debug\
obscured business rules\
hard to reuse\
leads to duplication (because it's hard to reuse)\
many reasons to change (and still hard to test!)\
can't be optimized\ 
mixed levels of abstraction\ 
lack cohesion, high coupling\

### How Long to Make Methods?
SLAP: single level of abstraction

All code in a method should operate on the same level of abstraction.\
Don't mix high-level calls with nitty-gritty byte parsing.\
Put byte parsing in a method that only does nitty-gritty stuff\
(Thoughts: keep a sort of level of abstraction-cohesiveness) 

Comment _why_, not _what_\
If you need to comment _what_, you need to refactor

## Don't Violate the Open-Close Principle
Open for extension; closed from modification

Closed from modification: don't change older code when adding new features\
Open for extension: still add new features through polymorphism, reflection and loose coupling 

**Code is extensible for some particular use case, not infinitely extensible.**\
Too extensible out-of-the-box makes things overly complex (Thought: and YAGNYet)

How to know how extensible to make it? Need both:

	* know software: know the limitation of the language, frameworks 
	* know domain: understand what could be probably extended (e.g. might have a car with more or less seats, probably not have a car with more than 1 roof)


Find domain expert to understand what could be extended.\
If we can't figure out it, use YAGNYet, and make it extensible when needed, at the last responsible moment. 

## Liskov's Substitution Principle
(Wiki: Liskov's notion of a behavioral subtype defines a notion of substitutability for objects; that is, if S is a subtype of T, then objects of type T in a program may be replaced with objects of type S without altering any of the desirable properties of that program)

Inheritance should be used only for subsistutability.

If B needs to use A, use composition.\
If B can be used everywhere A can be used, use inheritance. 

Services of the derived class should require no more and promise no less than the corresponding services of the base class.\
(Thoughts: derived class should be a fully unnoticed change for the code around it)

The user of a base class should be able to use an instance of a derived class without knowing the difference.\
(thoughts: 'cause you change less shit everywhere)





