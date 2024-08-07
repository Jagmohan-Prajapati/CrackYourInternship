"""Given an array arr[] of length n. Find all possible unique permutations of the array in sorted order. A sequence A is greater than sequence B if there is an index i for which Aj = Bj for all j<i and Ai > Bi.
Example 1:
Input: 
n = 3
arr[] = {1, 2, 1}
Output: 
1 1 2
1 2 1
2 1 1

Explanation:
These are the only possible unique permutations
for the given array.

Example 2:
Input: 
n = 2
arr[] = {4, 5}
Output: 
Only possible 2 unique permutations are
4 5
5 4

Your Task:
You don't need to read input or print anything. You only need to complete the function uniquePerms() that takes an integer n, and an array arr of size n as input and returns a sorted list of lists containing all unique permutations of the array.

Expected Time Complexity:  O(n*n!)
Expected Auxilliary Space: O(n*n!)

Constraints:
1 ≤ n ≤ 9"""


class Solution:
    def uniquePerms(self, arr, n):
        def permute(nums):
            def backtrack(start):
                if start == len(nums):
                    result.add(tuple(nums[:]))
                    return
                for i in range(start, len(nums)):
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start + 1)
                    nums[start], nums[i] = nums[i], nums[start]

            result = set()
            backtrack(0)
            return result

        unique_perms = permute(arr)
        perm_list = sorted(unique_perms)
        return [list(perm) for perm in perm_list]