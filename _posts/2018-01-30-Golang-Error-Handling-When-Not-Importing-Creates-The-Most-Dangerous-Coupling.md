---
layout: post
title:  "Golang Error Handling: When Not Importing Creates The Most Dangerous Coupling"
---

I’m going to refer to a talk given by Dave Cheney ([Don’t Just Check Errors Handle Them Gracefully](https://www.youtube.com/watch?v=lsBF58Q-DnY&feature=youtu.be)) in which he presents his vision on Go error handling.


## Letting the Errors Guide Us

Most errors are effectively unhandled, simply rocketed ever-upwards to the ever-wiser calling function where enlightened error handling decisions can occur.

Some situations bless us with errors that can actually be handled e.g. we can retry a network connection, a file write, an HTTP call. How do we identify what error occurred and, more importantly, what can we actually do about it?

In his talk, around [11m40s](https://www.youtube.com/watch?v=lsBF58Q-DnY&feature=youtu.be&t=11m40s), Dave Cheney offers we should:


>Assert errors for behavior, not type.

That is, check if an error has a certain method available that can guide us in handling it.

For example, wouldn’t we smile contentedly if we knew an error was temporary. We could hope and retry:

```golang
err, value = http.Get()
if IsTemporary(err){
    //retry, possibly not immediatly
}
```

How would the error whisper to us that it’s temporary? An example of asserting behavior from the talk: we verify the error implements the temporary interface, and if so, we ask the error to tell us if it’s temporary by calling the Temporary() function

```golang
type temporary interface{
   Temporary() bool
}

// IsTemporary returns true if err is temporary
func IsTemporary(err error) bool{
   te, ok := err.(temporary)
   return ok && te.Temporary()
}
```

## Life Without Importing
The idea is quite elegant; I like it, and I’m willing to sit back and smile imagining its mainstream use.

The happiness lasts until around [12m57s](https://www.youtube.com/watch?v=lsBF58Q-DnY&feature=youtu.be&t=12m57s) where Dave Cheney says:

>The key here is that all of this logic can be implemented **without importing the package that created this error** or indeed knowing anything about the error’s underlying type. All we’re interested in is its behavior.

At first glance, this sounds like a feature: we annihilate our high-profile enemy that is coupling. Unmitigated victory!

## Next Generation Coupling: Manual Coupling

We turn around to realize we had defeated a shadow of the real colossus now before us: *manual coupling*.

What happens if a new version of the vendor package changes the error’s method, say from *Temporary()* to *XtremelyTemporary()*? Well, our interface temporary, which only knows about the *Temporary()* method, certainly won’t automatically know about this change. Given such a rename, anything using the *temporary* interface will effectively silently fail to work as expected; there will be a stealthy mismatch between the interface and the error’s method.

We have thus created manual coupling: someone will need to dutifully read the docs or source code every time vendor packages are updated, to ensure our *temporary* interface correctly reflects the error’s methods.

If only there was an entity, a tool, that could detect whether our code is referring to interfaces which have been changed in vendor packages. Wouldn’t you delegate this work to it?