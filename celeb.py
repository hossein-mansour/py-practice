# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:26:07 2020
should have used set instead of list for candidates
should also delete people
"""

#==============================================================================
def has_celebrity_best(M):
	N = len(M)
	candidates = list(range(N))
	while candidates:
		
		try:
			first = candidates.pop()
		except:
			return False
		try:
			second = candidates.pop()
		except:
			if sum(M[first])==0 and sum([x[first] for x in M])==N-1:
				return True
			
		if M[first][second]==0 and M[second][first]==1:
			candidates.append(first)
		elif M[first][second]==1 and M[second][first]==0:
			candidates.append(second)
	return False		

#==============================================================================
def has_celebrity_O_N(M):
	N = len(M)
	candidates = set(range(N))
	while candidates:
		candidate = next(iter(candidates))
		row_ok = True
		for i in range(N):
			if candidate == i:
				continue
			if M[candidate][i]==0:
				try:
					candidates.remove(i)
				except:
					pass
			else:
				candidates.remove(candidate)
				row_ok = False
				break
		if row_ok:
			col=[x[candidate] for x in M]
			col_ok = True
			for j in range(N):
				if candidate == j:
					continue
				if col[j]==1:
					try:
						candidates.remove(j)
					except:
						pass
				else:
					candidates.remove(candidate)
					col_ok = False
					break
			if col_ok:
				print(str(candidate) + " is a celebrity")
				return True
	print("There is no celebrity")		
	return False		
#==============================================================================
def has_celebrity_O_N_squared(M):
	N = len(M)
	for i in range(N):
		if sum(M[i])==0 and sum([x[i] for x in M])==N-1:
			return True
			break
	return False

#==============================================================================


M=[[0,1,1,0],[0,0,0,0],[0,1,0,1],[0,1,0,0]]
print(has_celebrity_best(M))