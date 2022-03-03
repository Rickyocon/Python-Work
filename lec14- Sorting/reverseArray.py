def reverse_arr(arr):

	idx1 = 0; #index for the 1st element in swap
	idx2 = len(arr)-1 # index of the 2nd element in swap

	#loop for len//2 times
	for x in range(len(arr)//2):

		# 1.) swap the two elements
		tmp = arr[idx1]; #temperary varable (place holder)
		arr[idx1] = arr[idx2];
		arr[idx2] = tmp;

		#2.) update the two index vars
		idx1 += 1;
		idx2 -= 1;

# Main program
a1 = [3, 2, 1, 0, 5, 6]
reverse_arr(a1);
print(a1); 
		
		
