# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 18:25:11 2020

@author: hosse
"""


def cont_sum(L,des_sum):
	start = 0
	end = 0
	current_sum = 0
	N = len(L)
	while end<N-1:
		if current_sum<des_sum:
			end += 1
			current_sum += L[end]
		elif	current_sum == des_sum:
			return((start,end))
		else:
			while current_sum>des_sum:
				current_sum -= L[start]
				start += 1
	return False
			