## Feedback

* Good!
* In your `__and__` function, the comment should say "intersection", not "union"
* On lines 45-47, cleaner would be: `if not self.contains(otherEle)`
* It looks like you started writing another method and then ran out of time, but that's ok

For the optional part, you can use the keyword `yield`:

	def __iter__(self):
		for i in self.list:
			yield i
