"""Given an array which contains integer values, we need to make all values of this array equal to some integer value with minimum cost where the cost of changing an array value x to y is abs(x-y). 

Examples : 
Input  : arr[] = [1, 100, 101]
Output : 100
We can change all its values to 100 with minimum cost,
|1 - 100| + |100 - 100| + |101 - 100| = 100

Input  : arr[] = [4, 6]
Output : 2
We can change all its values to 5 with minimum cost,
|4 - 5| + |5 - 6| = 2
"""

# Python3 program to find minimum 
# cost to make all elements equal

# Utility method to compute cost, when
# all values of array are made equal to X
def computeCost(arr, N, X):

	cost = 0
	for i in range(N):
		cost += abs(arr[i] - X)
	return cost


# Method to find minimum cost to 
# make all elements equal
def minCostToMakeElementEqual(arr, N):

	low = high = arr[0]

	# Setting limits for ternary search 
	# by smallest and largest element
	for i in range(N):
	
		if (low > arr[i]): low = arr[i]
		if (high < arr[i]): high = arr[i]


	# loop until difference between low and 
	# high become less than 3, because after 
	# that mid1 and mid2 will start repeating
	while ((high - low) > 2):
	
		# mid1 and mid2 are representative 
		# array equal values of search space
		mid1 = low + (high - low) // 3
		mid2 = high - (high - low) // 3

		cost1 = computeCost(arr, N, mid1)
		cost2 = computeCost(arr, N, mid2)

		# if mid2 point gives more total
		# cost, skip third part
		if (cost1 < cost2):
			high = mid2

		# if mid1 point gives more total 
		# cost, skip first part
		else:
			low = mid1
	

	# computeCost gets optimum cost by 
	# sending average of low and high as X
	return computeCost(arr, N, (low + high) // 2)

# Driver code
arr = [1, 100, 101]
N = len(arr)
print(minCostToMakeElementEqual(arr, N))