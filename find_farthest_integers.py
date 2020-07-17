# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:19:20 2020

@author: hosse
"""

def find_farthest_integers(l: list) ->tuple:
	N = len(l)
	start = 0
	end = N-1
	min_alfa = l[0]
	max_beta = l[-1]
	while min_alfa > max_beta:
		start += 1
		end = N - 1 - start
		min_alfa = min(min_alfa,l[start])
		max_beta = max(max_beta,l[end])

	for new_start in range(start+1):
		new_end = N - 1 - new_start
		if l[new_start]<=l[end]:
			return new_start,end
		elif l[start]<=l[new_end]:
			return start, new_end
l = [11,2,2,12,1,2]

if __name__ == "__main__":
	print(find_farthest_integers(l))
		
	