## First Impressions of Golang: Error Handling
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


Point is that errors are not errors as a construct of the language but purely errors by convention: they're called 'err' or 'error', they implement an interface called 'Error' or 'MyBiggestMistakeYet', they have meaningful a value when shit goes wrong and unexiciting values otherwise, etc.

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
#### Visual Noise
My first issue, fairly subjective, is that this error handling is pretty noisy. Because errors are not special to the language, their handling looks like normal operations.

I feel that clarity is lost when trying to understand the intention of the code. In the prior example, the code not dealing with errors is always at the same level of indentation; however, when conditional statements and loops kick in, indentation is no longer an indicator of normal code or error handling code.

It's up to the programmer, when trying to understand a function, to not only read Go (which is pretty verbose) but to additionally backtrack when falling into error handling, which happens as often as function calls. Because errors aren't special or attached to any keywords, IDEs (currently) don't provide any specific highlighting, which would help with the noise. I confess this might be just a problem for non-C, non-Go programmers but it's frustrating me at the moment.

#### Lack of Actual Handling
It's noisy but it's worth it, isn't it?

As the Golang Blog says:
>The language's design and conventions encourage you to explicitly check for errors where they occur.

That's very true indeed, when you inspect that `err` return value, you're pushed to immediatly process this error.

However, the vast majority of the time, I see (vastly oversimplified):
```golang
func SomeFunction() error {
	var value int
	var err error
	value, err = someOperation()
	if err != nil {
		return err
	}

	for key, value = range someArray {
		err = someOperation2(value)
		if err != nil {
			return err
		}
	}

	value, err = someOperation3()
	if err != nil {
		return err
	}
	if value == 1 {
		value, err = someOperation5()
		if err != nil {
			return err
		}
	} else {
		value, err = someOperation6()
		if err != nil {
			return err
		}

	}

	return nil
}
```
Is that really error handling?

It feels that many functions, especially lower-level ones, can't do so much; a pretty big chunk of the codebase ends up looking like that. Maybe it's the codebases I've seen, but generally, you tend to bubble up the errors to a parent a few levels up that can make an actual decision on how to proceed, what other functions to use to remediate the situation, how to fail gracefully. 

**So the error mechanism seems to be built for a small portion of the codebase.**

There's this except from this [keynote adaptation from 2012](https://talks.golang.org/2012/splash.article#TOC_16.):

>There is no question the resulting code can be longer, but the clarity and simplicity of such code offsets its verbosity. Explicit error checking forces the programmer to think about errors — and deal with them — when they arise. Exceptions make it too easy to ignore them rather than handle them, passing the buck up the call stack until it is too late to fix the problem or diagnose it well.

This is where I tend to disagree with their perspective (it's called being irrevocability correct). Go's error handling scheme does not actually **force the handling of the error** and does not **force the programmer to deal with them when they arise**. Indeed, drowning the code with:

```golang
if err != nil{
return err
}
```

Is essentially a more verbose way of just not catching any exceptions.

Is it a good idea to handle the errors? Yes. Is it a good idea deal with them when they arise? Sometimes.

However, if the language user does not want to, they will not. In fact, they can just ignore the error altogether and never check it. Of course, the programmer is inched towards doing the right thing but if the good practices are absent, I don't feel this feautre will make a difference.

I currently feel the tradeoff is not worth it. The verbosity and lack of error flow actually adds to my confusion when reading the codebase. Rarely have I seen errors immediatly handled, they're usually handled by a caller some levels up.


#### Why Not Exceptions? 
I was at first intrigued as to why Golang decided not to make use of Exceptions, so I tried to find some explanations. I couldn't find much but here it is.

The [Golang FAQ](https://golang.org/doc/faq#exceptions) and  [keynote adaptation from 2012](https://talks.golang.org/2012/splash.article#TOC_16.) touch on exceptions.

Essentially, and without much explanation as far as I can read, they view Exceptions as encouraging errors to be ignored or handled too late, which I've seen happen anyway in Go. They also view exceptions as creating convoluted program flow, which I so far think is more a consequence of poor program design in general, not of Exceptions.

So far, I haven't felt that handling errors using Go's mechanism has created less convoluted flows.


#### Go's View on Errors in Computer Programs
Still from the [keynote adaptation from 2012](https://talks.golang.org/2012/splash.article#TOC_16.):
>[There] is nothing truly exceptional about errors in computer programs. For instance, the inability to open a file is a common issue that does not deserve special linguistic constructs; if and return are fine.

I think that this is really the meat of the argument: whether errors deserve special treatment.

My current view of the flow of execution is that the function makes certain assumptions about the state of the ressources it's accessing, and interactions it's having. Functions make these assupmtions and if the assumptions are wrong beyond a certain narrow angle, the functions need to fail. 

I look at this as a matter of responsability; let's take the example of the inability to open a file. Let's suppose a function needs to open a file, read the data, perform some validation and store it.

If the file is not readable, why has it become our function's problem to make it readable? It's simply not its responsability to do so. Making the file readable might involve a certain number of operations, including asking the user to change permissions, or changing the permissions automatically. 

So, currently, my view is that errors are exceptional: they occur when the assupmtions about the world are incorrect. A function was built based on these world-assumptions and correcting them all immediatly or near-immediatly is very much past the scope of that function's responsability.


#### Exceptions can be Immediate Too
I imagine that the fear of try-catch-finally looks something like this (I have to imagine because I haven't found an analysis of the fear):

```python
try:
    # millions of lines of code

except Exception as e:
    raise e
```

However, that's not the only reality Exceptions offer.
In a more Go-like manner, we could pseudo-have
```python
try:
	fd = openFile(filePath)
except IOError as e:
	#do whatever


try:
	validate(fd)
except Exception1:
	#handle it
except Exception2:
	#handle it
```

If we don't mind verbosity, and clearly with Go we don't, exceptions can easily be used to do immediate handling of errors/exceptions.

#### A Technological Solution to a Cultural Problem?
In the end, I wonder if Go is trying to address a deficiency in the user of the langauge: poor error handling. 

It seems to me that Exceptions are just a tool, and if you use it poorly, you'll get poor results. In the same vein, Go's error handling is also just a methodology, and if used improperly, you'll still get poor results.

Go's error handling doesn't really force the careless programmer to do anything, except flood `return err` everywhere (or just not check for errors at all) and only handle errors when something breaks, just like they would with exceptions.






