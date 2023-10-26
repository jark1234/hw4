def merge_list(list1, list2):
	if not (isinstance(list1, list) and isinstance(list2,list)):
		raise TypeError("Inputs should be lists.")
	for num in list1 + list2:
		if not isinstance(num, int):
			raise TypeError("List contains non-intergers.")
		merge = list1 + list2
	n = len(merge)
	for i in range(n):
		for j in range(0, n-i-1):
			if merge[j] > merge[j+1]:
				merge[j], merge[j+1] = merge[j+1], merge[j]	
	return merge
