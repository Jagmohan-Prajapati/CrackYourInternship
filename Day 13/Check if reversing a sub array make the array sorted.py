"""Given an array of n distinct integers. The task is to check whether reversing any one sub-array can make the array sorted or not. If the array is already sorted or can be made sorted by reversing any one subarray, print “Yes“, else print “No“.

Examples: 

Input : arr [] = {1, 2, 5, 4, 3}
Output : Yes
By reversing the subarray {5, 4, 3}, the array will be sorted.

Input : arr [] = { 1, 2, 4, 5, 3 }
Output : No"""

# Python3 program to check whether 
# reversing a sub array make the 
# array sorted or not 

# Return true, if reversing the 
# subarray will sort the array, 
# else return false. 
def checkReverse(arr, n): 

	# Copying the array 
	temp = [0] * n 
	for i in range(n): 
		temp[i] = arr[i] 

	# Sort the copied array. 
	temp.sort() 

	# Finding the first mismatch. 
	for front in range(n): 
		if temp[front] != arr[front]: 
			break

	# Finding the last mismatch. 
	for back in range(n - 1, -1, -1): 
		if temp[back] != arr[back]: 
			break

	#If whole array is sorted 
	if front >= back: 
		return True
	while front != back: 
		front += 1
		if arr[front - 1] < arr[front]: 
			return False
	return True

# Driver code 
arr = [1, 2, 5, 4, 3] 
n = len(arr) 
if checkReverse(arr, n) == True: 
	print("Yes") 
else: 
	print("No") 