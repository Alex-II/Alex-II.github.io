# First Impressions in Golang
For about two months now, I've both reworked other people's code and created my own code (that will be considered legacy soon enough). Naturally, I've begun to develop an opinion (that I know can only be right) based on experience with Go so far.

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
In theory, Go very much encourages you to handle errors right there and then, nearest the function that errored out.
The [Golang Blog](https://blog.golang.org/error-handling-and-go) explains :

>In Go, error handling is important. The language's design and conventions encourage you to explicitly check for errors where they occur (as distinct from the convention in other languages of throwing exceptions and sometimes catching them). In some cases this makes Go code verbose, but fortunately there are some techniques you can use to minimize repetitive error handling.

Indeed, let's assume your function signature is `func SomeFunction() error` ; this means the function takes no arguments and returns an `error` (in this case, `error` is an interface from the std lib so the func returns something that implements that interface).

```golang
func SomeFunction() error {
	var value int
	var err error
	value, err = someOperation()
	if err != nil {
		return err // (1) we just forward the error upwards
	}

	value, err = someOperation2()
	if err != nil {
		// (2) we add some context, then forward the error
		return fmt.Errorf("Could not do the intended thing with the thing : %v", err)
	}

	value, err = someOperation3()
	if err != nil {
		// (3) we know the error exposes more details, we can take action right away
		switch err {
		case InsufficientPraying:
			SomeGracefulFailure()
			return fmt.Errorf("couldn't some operation the 3rd, graceful failed : %v", err)
		case NotEnoughLuck:
			SomeOtherGracefulFailure()
			return fmt.Errorf("couldn't some operation the 3rd, graceful failed the other way : %v", err)
		default:
			return fmt.Errorf("unexpected some operation the 3rd failure : %v", err)
		}
	}

	value, err = someOperation4(value)
	if err != nil {
		// (4) because the error can be whatever, it might contain functions or advanced magic
		if preferSafety {
			err.Rollback() 
			return fmt.Errorf("failed to some operation with value %d, performed best effort rollback : %v", value, err.State)
		}
		return fmt.Errorf("failed to some operation with value %d, did not perform rollback : %v", value, err.State)

	}

	return nil
}
```
### What's the Problem?


The [Golang FAQ](https://golang.org/doc/faq#exceptions) discussed why Exceptions were not included in Go, here is an excerpt:
> We believe that coupling exceptions to a control structure, as in the try-catch-finally idiom, results in convoluted code. It also tends to encourage programmers to label too many ordinary errors, such as failing to open a file, as exceptional

