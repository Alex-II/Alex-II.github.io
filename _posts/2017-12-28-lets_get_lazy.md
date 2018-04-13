---
layout: default
title: "Let’s Get Lazy—The Real Power of Functional Programming - Venkat Subramaniam [Talk]"
category: notes
---

# [Let’s Get Lazy—The Real Power of Functional Programming by Venkat Subramaniam](https://www.youtube.com/watch?v=ntWdmlrCheY)

## What does Lazy mean?
We postpone evaluating an expression.  
Because we may not need to evaluate at all in some cases.

## Applicative Order vs Normal Order
### Applicative Order
Eager evaluation that, for example, evaluates expressions passed as arguments to functions immediately, and then calls the function with the result

```c
int a(int p){
   return p + 3;
}

int b(int q){
  return q + 4;
}

//in this case, a(4) is evaluated first
//then the result is immediately passed to b()
b(a(4)); 
 
```

### Normal Order
**Lazy evaluation**, where expressions are only evaluated at the last possible moment

```c
int a(int p){
  return p + 3;
}

int b(int q){
  return q + 4;
}

int c(int s){
  return 7;
}

//in this case, a(4) is evaluated only if b() makes use of it
//otherwise, it's never evaluated
b(a(4)); 

//in this case, a(4) would not be evaluated at all
// because c() doesn't actually use the variable 's' bound to the result of a(4)
c(a(4)); 
```

## Lazy Evaluation Needs Purity
Unevaluated expressions are carried around until postponed evaluation.  
If they depend on an external element whose value might change between the time they are given to be carried around and the time they are evaluated, the result might be unanticipated. 

E.g. A lazily evaluated function uses a variable that is declared outside the function's scope.
The variable's value changes.
The function is finally evaluated and uses that variable, whose value is no longer the same as when the function was first given the variable.

## Born Lazy, Born Eager
Some languages like Haskell need you to fight to allow mutability
Some languages like C#, Java need you to fight to get pure functions and lazy behavior

(Thoughts: it feels like C# and Java lazy-features are programmer-space while lazy-features in Haskell are in compiler-space)

## Laziness in Collections and No Performance Loss
Because of the laziness, easy to read code doesn't suffer performance hits (in right languages, such as Java, C#)

In C# for example, piped (chained) functions evaluate lazily as possible 

Let's say we want the square of the first number that's greater than 3 and even

```java
List<int> numbers = new List<int>{ 1, 2, 3, 5, 4, 6, 6, 7, 8, 9 }

// Given a list of integers of length n
// You'd think this would be O(3n) or such
// As in, you'd find all the >3 in the list,
// then all the even ones among them,
// the double them all, then pick the first
// but..
Console.WriteLine(
   numbers.Where(IsGT3) //instead only 1,2,3, 5, and 4 reach here 
          .Where(IsEven) // only 5 and 4 reach here
          .Select(DoubleIt) // 4 gets doubled
          .First()); // done

public static bool IsGT3(int number){
   return number > 3;
}

public static bool IsEven(int number){
   return number%2 == 0;      
}

public static int DoubleIt(int number){
     return number * 2;      
}
```
But not all languages are made the same... some languages don't do that as well as that

## Easy to Read
It's really a delight to read, boilerplate abstracted away, temp variables hidden, meaning surfaces


