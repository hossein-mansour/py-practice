# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 12:24:20 2020

@author: hosse
"""
from functools import lru_cache
@lru_cache(maxsize=None)
def fib_rec(n: int) ->int:
	if n<2:
		return n
	else:
		return fib_rec(n-1) + fib_rec(n-2)

def fib_simple(n):
	fibs = []
	for i in range(n+1):
		if i<2:
			fibs.append(i)
		else:
			fibs.append(fibs[-1]+fibs[-2])
	return fibs[-1]
			
#yield could be put outside the loop so that fib_gen behaves similar to fib_simple
def fib_gen(n):
	if n==0: yield 0
	if n == 1: yield 1
	last = 1
	one_to_last = 0
	for _ in range(1,n):
		one_to_last , last = last, last+one_to_last
		yield last
	
	
	

if __name__ == "__main__":
	print(fib_rec(50))
	print(fib_simple(50))
	print(*fib_gen(50))
	
	
	