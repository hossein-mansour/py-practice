# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 07:40:40 2020

@author: hosse
"""

def compute_pi (n_terms: int) -> float:
	pi = 0
	num = 4
	den = 1
	mult = 1
	for n in range(n_terms):
		pi += mult * num/den
		den+=2
		mult *= -1
	return pi

print(compute_pi(10000))