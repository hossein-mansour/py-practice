#bubble sort
def bubble_sort(li) -> list:
	is_sorted = False
	so_far = 0
	while not is_sorted:
		is_sorted = True
		for ind in range(len(li)-so_far-1):
			if li[ind]>li[ind+1]:
				li[ind],li[ind+1] = li[ind+1],li[ind]
				is_sorted = False
		so_far += 1
	return li

def merge_sort(li: list) -> list:
	if len(li) == 1:
		return li
	else:
		mid = len(li)//2
		left = merge_sort(li[:mid])
		right = merge_sort(li[mid:])
		sorted_list = []
		left_pt = 0
		right_pt = 0
		while (left_pt < len(left)) or (right_pt < len(right)):
			if left_pt == len(left):
				sorted_list.append(right[right_pt])
				right_pt+=1
			elif right_pt == len(right):
				sorted_list.append(left[left_pt])
				left_pt+=1
			else:
				if right[right_pt]<left[left_pt]:
					sorted_list.append(right[right_pt])
					right_pt+=1
				else:
					sorted_list.append(left[left_pt])
					left_pt+=1
		return sorted_list
	
def quick_sort_in_place(my_list,left_bound,right_bound):
	import random
	if (left_bound < right_bound):
		pivot_pt = random.randint(left_bound, right_bound)
		pivot = my_list[pivot_pt]
		left_pt = left_bound
		right_pt = right_bound
		while left_pt<=right_pt:
			if my_list[left_pt]>=pivot and my_list[right_pt]<=pivot:
				my_list[left_pt],my_list[right_pt]=my_list[right_pt],my_list[left_pt]
			if my_list[left_pt]<=pivot:
				left_pt+=1
			if my_list[right_pt]>=pivot:
				right_pt-=1
		quick_sort_in_place(my_list,left_bound,left_pt-1)
		quick_sort_in_place(my_list,left_pt,right_bound)

def quick_sort(li):
	import copy
	import random
	my_list = copy.copy(li)
	if len(my_list) > 1:
		pivot_pt = random.randint(0, len(my_list)-1)
		pivot = my_list[pivot_pt]
		left_pt = 0
		right_pt = len(my_list)-1
		
		while left_pt<=right_pt:
			if my_list[left_pt]>=pivot and my_list[right_pt]<=pivot:
				my_list[left_pt],my_list[right_pt]=my_list[right_pt],my_list[left_pt]
			if my_list[left_pt]<=pivot:
				left_pt+=1
			if my_list[right_pt]>=pivot:
				right_pt-=1
		my_list = quick_sort(my_list[:left_pt]) + quick_sort(my_list[left_pt:])
	return my_list
			
def selection_sort(li):

	def find_min(this_list,ind):
		min_ind = ind
		for current_ind in range(ind,len(this_list)):
			if this_list[current_ind]<this_list[min_ind]:
				min_ind = current_ind
		return min_ind
	
	for pt in range(len(li)-1):
		min_ind = find_min(li,pt)
		li[pt],li[min_ind]= li[min_ind],li[pt]

def insertion_sort(li):
	for i in range(1,len(li)):
		for j in range(i):
			if li[j]>li[i]:
				li = li[:j]+[li[i]]+li[j:i]+li[i+1:]
	return li
		

if __name__ == "__main__":
	import random
	import copy
	my_list = random.sample(range(1,100),10)
	print(*my_list)
		
	li = copy.copy(my_list)
	print(*bubble_sort(li))
	print(*merge_sort(my_list))
	print(*quick_sort(my_list))
	li = copy.copy(my_list)
	quick_sort_in_place(li,0,len(li)-1)
	print(*li)
	li = copy.copy(my_list)
	selection_sort(li)
	print(*li)
	
	li = copy.copy(my_list)
	print(*insertion_sort(li))