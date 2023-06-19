"""
https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Strategy:
        1. Use two pointer: left, right to indicate the left bound and
        right bound of the window.
        2. If values in windows smaller than target,
            expand the windows.
        3. If values in windows bigger the target,
            then we find a possible answer.
        4. but we need to keep finding others possible answer,
            So windows move forward, left +=1.
            If still bigger, left forward.
            If smaller, right forward.
        """
        ans = float("inf")
        left = 0
        total = 0  # keep values go throught until now.
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1

        if ans == float("inf"):
            return 0
        return ans
