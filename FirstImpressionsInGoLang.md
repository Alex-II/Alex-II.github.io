# First Impressions in Golang
For about two months now, I've both reworked other people's code and created my own code (that will be considered legacy soon enough). Nautrally, I've begun to develop an opinion (that I know can only be right) based on experience with Go so far.

## Prelude: Who Dares
I'm not a language designer, I don't have five centuries of software engineering experience, so take these views as those of a common language user with two months of experience. It's first impressions. I hope to return six, twelve months from now and explain why my first impressions were ~~luck~~ genius or retort adequately.

I've been nursed by Python, C#, JavaScript and C++.

## Error Handling
Go functions can return several values and Go uses this to better follow C's creed about errors being exposed as function return values. As exceptions don't exist in Go we have something of this sort:
```
resultValue, err = SomeOperation()
```
By convention `err` is `nil` (null) if the function completed successfully and is not `nil` otherwise.

Error objects are not special in any way really, they are just a variable like any other (unlike Exceptions, in C#, Python, Java, etc).
The type of that error variable usually implements an Error interface (of the standard lib) but could implement any interface really (or be entirely orphan to any interface).
An "error" variable could be an any type really: an int, a byte, an IP, a FileReader, a BananaFactory.
Point is: errors are not errors as a construct of the language but purely errors by convention: they're called 'err' or 'error', they implement an interface called 'Error' or 'MyBiggestMistakeYet', they have meaningful a value when shit goes wrong and unexiciting values otherwise, etc.

### Why
In theory, this means that Go very much encourages you to handle the error right there and then, nearest the function that errored out.
The [Golang Blog](https://blog.golang.org/error-handling-and-go) explains :

>In Go, error handling is important. The language's design and conventions encourage you to explicitly check for errors where they occur (as distinct from the convention in other languages of throwing exceptions and sometimes catching them). In some cases this makes Go code verbose, but fortunately there are some techniques you can use to minimize repetitive error handling.

In practice, what I have noticed is a great deal of the following.


The [Golang FAQ](https://golang.org/doc/faq#exceptions) discussed why Exceptions were not included in Go, here is an excerpt:
> We believe that coupling exceptions to a control structure, as in the try-catch-finally idiom, results in convoluted code. It also tends to encourage programmers to label too many ordinary errors, such as failing to open a file, as exceptional

