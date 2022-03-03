from arrOps import *;

def bubble_sort(arr):
	#-------------------------------------------------------------------------
	# your job here
	# INCOMPLETE: 2-layer nested loop
	#INSIDE this nested loop
	n = len(arr);
	for x in range(n):
		for i in range(n-1):
			if arr[i] > arr[i+1]:
				#SWAP
				tmp = arr[i];
				# REPLACE with setArrElement
				setArrElement(arr, i, arr[i+1]);
				# REPLACE with setArrElement(____, _____, ____) 
				setArrElement(arr, i+1, tmp);
	#-------------------------------------------------------------------------
	return arr;

arr1 = [100, 150, 200, 120, 300, 250, 240, 230, 130, 300, 200, 330,
	340, 240, 120, 230, 350, 110, 220, 250, 320, 270];
drawArr(arr1);
input("Enter to continue sort!");
bubble_sort(arr1);
input("Enter to complete!");
