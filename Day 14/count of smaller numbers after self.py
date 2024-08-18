"""Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

Example 1:
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Example 2:
Input: nums = [-1]
Output: [0]

Example 3:
Input: nums = [-1,-1]
Output: [0,0]
 
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104"""

from array import array

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = array('i', bytes(len(nums) << 2))
        nums2 = array('h')

        for i in range(l-1,-1,-1):
          n = nums.pop()
          lpos = bisect_left(nums2, n)
          ans[i] = lpos
          nums2.insert(lpos, n)

        return ans