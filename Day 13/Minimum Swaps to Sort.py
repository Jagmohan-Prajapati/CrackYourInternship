"""Given an array of n distinct elements. Find the minimum number of swaps required to sort the array in strictly increasing order.

Example 1:
Input:
nums = {2, 8, 5, 4}
Output:
1
Explanation:
swap 8 with 4.

Example 2:
Input:
nums = {10, 19, 6, 3, 5}
Output:
2
Explanation:
swap 10 with 3 and swap 19 with 5.

Your Task:
You do not need to read input or print anything. Your task is to complete the function minSwaps() which takes the nums as input parameter and returns an integer denoting the minimum number of swaps required to sort the array.
If the array is already sorted, return 0. 

Expected Time Complexity: O(nlogn)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ n ≤ 105
1 ≤ numsi ≤ 106"""

class Solution:
    def minSwaps(self, nums):
        n = len(nums)
        arrpos = [(num, i) for i, num in enumerate(nums)]
        arrpos.sort(key=lambda it: it[0])
            
        visited = [False] * n
        ans = 0
            
        for i in range(n):
            if visited[i] or arrpos[i][1] == i:
                continue
                    
            cycle_size = 0
            j = i
                
            while not visited[j]:
                visited[j] = True
                j = arrpos[j][1]
                cycle_size += 1
                    
            if cycle_size > 0:
                ans += (cycle_size - 1)
            
        return ans