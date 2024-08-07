"""Given an integer array nums, return the number of reverse pairs in the array.A reverse pair is a pair (i, j) where:0 <= i < j < nums.length and nums[i] > 2 * nums[j].
Example 1:
Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1

Example 2:
Input: nums = [2,4,3,5,1]
Output: 3
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1
 

Constraints:
1 <= nums.length <= 5 * 104
-231 <= nums[i] <= 231 - 1"""


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        def merge(left_arr, right_arr):
            i, j = 0, 0
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] > 2 * right_arr[j]:
                    self.count += len(left_arr) - i
                    j += 1
                else:
                    i += 1
            # Step 2: Merge sort left and right
            l, r = 0, 0
            res = []
            while l < len(left_arr) and r < len(right_arr):
                if left_arr[l] < right_arr[r]:
                    res.append(left_arr[l])
                    l += 1
                else:
                    res.append(right_arr[r])
                    r += 1
            return res + left_arr[l:] + right_arr[r:]
        def divide(arr):
            if len(arr) <= 1: return arr
            # divide the input array into 2 parts
            mid = len(arr)//2
            left_arr = divide(arr[:mid])
            right_arr = divide(arr[mid:])
            return merge(left_arr, right_arr)
        nums = divide(nums)
        return self.count