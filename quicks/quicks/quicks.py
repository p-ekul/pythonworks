def quick_sort(list):
	if len(list) <= 1 : return list
	pivot = list[len(list) // 2]
	less_arr,equal_arr,big_arr = [],[],[]
	for i in list:
		if i < pivot : less_arr.append(i)
		elif i>pivot : big_arr.append(i)
		else: equal_arr.append(i)
	return quick_sort(less_arr) + equal_arr + quick_sort(big_arr)
	
list = [11,6,2,8,7,9,5,14,22,34]
print("quicksorted", quick_sort(list))
	#quicksort
