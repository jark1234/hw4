def reverse_sort_dictionary(directory)
	if not isinstance(directory, dict):
		raise TypeError("Input should be a dictionary.")
	sorted_list = [(name, details[0]) for name, details in sorted(directory.items(), key=lambda x: x[0], reverse=True)]
	return sorted_list
