#!/usr/bin/env python3

# Example 1: Using looping technique
def fib(n):
	a,b = 1,1
	for i in range(n-1):
		a,b = b, a+b
	return a

# Example 2: Using recursion
def fib_rec(n):
	if n == 1 or n == 2:
		return 1
	else:
		return fib_rec(n-1) + fib_rec(n-2)

# Example 3: Using generators
a,b = 0,1
def fib_gen():
	global a,b
	while True:
		a,b = b, a+b
		yield a

# Example 4: Using memoization
def fib_memo(fn, arg):
	memo = {}
	if arg not in memo:
		memo[arg] = fn(arg)
	return memo[arg]

# Example 5: Using memoization as decorator
class Memoize:
	def __init__(self, fn):
		self.fn = fn
		self.memo = {}
	def __call__(self, arg):
		if arg not in self.memo:
			self.memo[arg] = self.fn(arg)
			return self.memo[arg]

@Memoize
def fib_dec(n):
	a,b = 1,1
	for i in range(n-1):
		a,b = b, a+b
	return a

print('### Nth fibonacci number')
print('# Example 1: Using looping technique')
print(fib(7))
print('# Example 2: Using recursion')
print(fib_rec(7))
print('# Example 3: Using generators')
f = fib_gen()
next(f) # Syntax for python3 instead of f.next()
next(f)
next(f)
next(f)
next(f)
next(f)
print(next(f))
print('# Example 4: Using memoization')
fibmemo = fib_memo(fib, 7)
print(fibmemo)
print('# Example 5: Using memoization as decorator')
print(fib_dec(7))
