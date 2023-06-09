"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""


class Solution:
    def twoSum(self, nums, target):
        """
        暴力解
        for n in nums:
            for m in nums:
                if n+m == target:
                    return [nums.index(n),nums.index(m)]
        """
        nums_dict = {}
        for index, value in enumerate(nums):
            find_target = target-value
            if find_target not in nums_dict:
                nums_dict[value] = index

            else:
                return [nums_dict.get(find_target), index]
