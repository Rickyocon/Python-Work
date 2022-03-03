def sel_sort(arr):
	n = len(arr);
	
	#LOOP: n passes
	for i in range(n):

		# 1.) find the min element from arr[i]..... to arr[n-1]
		# let idxMin be the index of that variable
		min = arr[i];		
		idxMin = i;
		for index in range(i, n):
			if arr[index] < min:
				min = arr[index];
				idxMin = index;
	
		# 2.) swap the element arr[i] with arr[idxMin]
		tmp = arr[i];
		arr[i] = arr[idxMin];
		arr[idxMin] = tmp;

# Main program
a1 = [5, 4, 3, 2, 1];
sel_sort(a1);
print(a1);

