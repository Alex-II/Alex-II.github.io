---
layout: default
title: "Speed without Discipline a Recipe for Disaster by Venkat Subramaniam [Talk]"
category: notes
---

# [Speed without Discipline a Recipe for Disaster by Venkat Subramaniam](https://www.youtube.com/watch?v=uQ75fI1tqoM)

## Sustainability
Can't be agile if you can't sustain pace


## Paradigm Shifts
90s shift: OOP  
Upcoming shift: Declarative programming 

## Imperative vs Declarative
<u>Imperative</u>  
What to do and how  
More complex, need to deal with low-level details  
Driving a manual-shift car to get to destination  

<u>Declarative</u>  
superset of Functional  
Focus on what to do, not on how to do it  
Using a driveless car to get to destination  

<u>Code example #1</u>

Imperative
```python
# list of names, which are 4 char long?
count = 0
for name in names:
  if len(name) == 4:
     count += 1

print(count)
```

Declarative
```python
# list of names, which are 4 char long?
print(len(list(filter(lambda x: len(x) == 4, names))
```

<u>Code example #2</u>

Imperative
```javascript
let element = $('#greet')
let name = 'Tom'
let message = name + ' how are you?'
element.val(message)
```

Declarative
```javascript
{
  selector: 'greet',
  template: '{{ name }} how are you?'
}
```
(Thoughts: declarative uses abstractions built on imperative; declarative has an implicit framework which is less transparent than imperative)  
(Thoughts: hope is that boilerplate imperative code (loops, ifs) could be replaced by some generic declarative code)

## Declarative Shift
Expressive  
Concise  
Maintainable  
Rapid Change  

## Testing Needed for Speed
In theory: respond to change even late in the dev cycle  
How can we sustain an attitude of late changes?

Use TDD to know whether fast-paced late changes work  
"I like to automate my tests not because I have a lot of time, it is because I don't"

## Testing vs Verification
Testing provides insight into the application: is it usable? is the workflow legit? UX? feel? should it be doing something else?  

Verification is used to check whether the code works or not.  
Manual verification: waste of the person's brain power, automated systems should do it  

Test manually, verify automatically

## 3 Phases of Automated Verification
### 1. no automation  
everything is manual verification, unsustainable as code grows, slower and slower

### 2) automation done wrong

![automation done wrong](/assets/speed_without_discipline_incorrect_automation.png)

Too many UI-level verification tests: too brittle, too slow, hard to write, hard to debug, are abandoned

(Thoughts: they essentially mirror what a human would do during manual verification; however, the UI is built for the human while it's a bigger struggle to master the UI-interaction programmatically. They're projecting the manual verification experience and trying to reproduce it in code)

### 3) automation at the right level, to the right measure, for the right reasons
![automation done right](/assets/speed_without_discipline_correct_automation.png)

## Why so hard to test the right way and hard to do TDD?
**i)"Code is hard to test" or "the design of the code sucks"**  
It's just not test friendly 

(Thoughts: it seems the UI-tests are popular precisely because of this: the entire system itself, through the UI, becomes the only level at which it's reasonable to test, all the other layers are broken in attempt to get the UI level to work nicely)

**ii) Can't think of tests before writing code**  
This is because we don't know what the code will look like.   
If we haven't touched a particular part of the technical domain, we're not sure what abstractions we'll use and what to expect of them

**To solve this, we need to do a Spike to Learn** 

Using a spike we explore the technical domain, we make our mini-experiments and make discoveries about the technical implications of the system we're trying to get to interact with, about the framework we're trying to master, about the interactions between many components. 

After the spike, we're ready to write the tests (as we just understood what to look for), and then the production code. We completely toss the code used for learning, it doesn't make it to production.   

It's write-rewrite but really learn-test-rewrite

## Making Testing and TDD Work

**Discipline**  
The dev is responsible for actually writing them and so casting blame on management is not a complete excuse  
There is a professional responsibility   
(Thought: you could argue management does think it understands and actively prohibits certain dev practices, even though it's not their responsibility to prohibit such things)

**Takes Time**  
i) Write the test themselves  
ii) Ramp up to using testing effectively  
(Thought: echoes a bit of Peopleware in which the author explain that people mistake the period of transition into a new system for the final state of the system)

**It's a Skill**  
Not magic, just another skill

**Culture**  
Need to create or find people who actually want to improve

**Excuses**  
It's like exercising, everyone knows it's good but everyone makes excuses not to do it

**Surgeries from 1820 Without Sterilization**   
Software today is like surgeries in 1820 when no one understood patients died of bacterial infection  
A lot of bad practices are performed out of ignorance









