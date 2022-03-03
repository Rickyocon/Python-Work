# void function
def bubble_sort(arr):

	# do n passes
	n = len(arr);
	for x in range(n):
		# compare each pair arr[i] and arr[i+1], swap if nessecary.
		# i: 0 to n-2
		for i in range(n-1):
			if arr[i]>arr[i+1]:
				tmp = arr[i] #TEMPERARY VARIABLE	
				arr[i] = arr[i+1];
				arr[i+1] = tmp;

#main program
a1 = [3, 2, 100, 0];
bubble_sort(a1);
print(a1);
