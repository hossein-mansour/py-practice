# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 09:24:35 2020

@author: hosse
"""
def paranthesis(s: str) -> bool:
	stack=[]
	for item in s:
		if item == '(':
			stack.append(item)
		elif item == ')':
			try:
				stack.pop()
			except IndexError:
				return False
	if not stack:
		return True
	else:
		return False
		
if __name__ == '__main__':
	my_string = 'slaam ( khanoom jan ) gjdsjgkrck ( ) )()'
	print(paranthesis(my_string))
