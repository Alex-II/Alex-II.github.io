---
layout: default
title: "Functional Programming with Java 8 by Venkat Subramaniam [Talk]"
category: notes
---

# [Functional Programming with Java 8 by Venkat Subramaniam](https://www.youtube.com/watch?v=15X0qFtBqiQ)

## Function Programming's Promise
We have

	* Inherent complexity: complexity stemming from domain
	* Accidental complexity: complexity we create when trying to deal with the inherent complexity 


**Functional programming removes much of the accidental complexity**

## Mutable State 
Code is becoming more concurrent 

Issues with mutable state:

	* Sharing mutable state is error prone
	* Mutable states are hard to reason about
	* Hard to make sequential code into concurrent code


## Functional Programming Properties
Functional is a layer of abstraction above imperative programming.

### Assignment-less Programming
Much like we don't use gotos in our code, but it's ok for the compiler to use gotos (or equivalent) under-the-hood

*goto is to imperative/structured programming*

what

*assignment is to functional programming*


### Immutable State
We can make smart copies of object.

Let the under-the-hood mutate the object, while we view and think of the object as immutable. 

### Functions as First-Class Citizens
We can treat functions like we do objects

A higher-order function can (one or more):

	* be passed functions as paramters
	* create functions itself
	* return functions

### Pure Functions
Pure functions don't have side-effects


	1. does not change some state outside its scope or has an observable interaction with its calling functions or the outside world besides returning a value, such as mutation of mutable objects (we want deterministic output to our input and the output is solely under the form of the returned value) [wiki, wiki, wiki]
	2. does not depend on anything that changes as well: The function result value cannot depend on any hidden information or state that may change while program execution proceeds or between different executions of the program
		* We want lazy evaluation

## Functional Style vs (Purely) Functional Programming 
Language provides higher-order functions: functional style (Java, C#)

Language prevents mutability: functional programming (Haskell) 

## Lambda Expression (Anonymous Function)
Only parameters list, body.

Inferred return, no name needed.

Passed to higher-order functions 

## Familiar vs Simple
**Complex (not simple) things seem easy to think about when they become familiar.
Familiarity with something does not imply that thing is simple.**

## External to Internal Iterators
<u>Given</u>
```
List<Integer> numbers = Arrays.asList(1,2,3,4,5,6,7,8,9,10);
```

<u>External Iterators</u>
```
for (int i = 0; i < numbers.size();  i++){
         System.out.println(numbers.get(i));
}
```

*OR*

```
for(int e: numbers){
   System.out.println(e);
}
```

<u>Internal Iterators</u>
Iteration on auto-pilot, no more boiler-plate 

Polymorphic because forEach() can change but you're not affected

```
numbers.forEach((Integer E) -> System.out.println(e));
```

Or even type inference in Java

```
numbers.forEach((e) -> System.out.println(e));
```


Or even method reference
```
numbers.forEach(System.out::println);
```

## Lazy Evaluation and Immutability 
<u>Given</u>
```
List<Integer> numbers = Arrays.asList(1,2,3);
```

We have a lambda that relies on the external array factor
```
int[] factor = new int[] { 2 };
Steam<Integer> strm = numbers.stream().map(e -> e * factor[0]);

factor[0] = 0 
strm.forEach(System.out::println)
```
This makes the lambda not pure; it relies on external elements that can change.

While we initially expected the printed output to be 2, 4, 6 we'll be getting 0,0,0
This is because the lazy evaluation happens after the change.

## Function Composition (Pipelining)
```
System.out.println(
   numbers.stream().
   .filter(e -> e % 2 == 0) // this is 
   .mapToDouble(Math::sqrt) // function composition (pipelining)
   .sum() //only evaluated here, not in any previous function of the pipeline
);
```

## Functional Benefits
<u>Code Clarity</u>: Easier to understand the intent 

<u>Fewer Errors</u>: No accidental complexity (thoughts: or just less)
Less mutability, as demanded by the functional style, also leads to less hard to see, hard to catch mutability errors

<u>Easier Parallelization</u>: In imperative, sequential code looks very different from concurrent. In functional, code structure is the same, with small simple and evident changes e.g.  one extra function in the pipeline

```
numbers.stream().
  .parallel()
  .filter(e -> e % 2 == 0) // this is
  .mapToDouble(Math::sqrt) // function composition (pipelining)
  .sum() //only evaluated here, not in any previous function of the pipeline
```


[Thoughts: Boilerplate is not needed, slips and mistakes in boilerplate is reduced

When certain imperative constructs become complex, there might be edge cases that aren't obvious

Without the need for continually coding very-similar-but-not-always identical boilerplate code, these non-obvious mistakes are prevented]




