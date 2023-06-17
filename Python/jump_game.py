"""
You are given an integer array nums. 
You are initially positioned at the array's first index, 
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. 
Its maximum jump length is 0, which makes it impossible to reach the last index.
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Strategy:
            1.set goal from "back",
            Eg.[2,3,1,1,4],
            if we can get second 1, means we can arrive 4.
            if we can get first 1m means we can arrive second 1.
            if we can get 3, means we get can arrive first 1.
            we can get 2 absolutely, so we can reach the last index. 
        return: can goal_index move to the first element.
        """
        if len(nums) == 1:
            return True

        goal_index = len(nums)-1
        for index in range(len(nums)-2, -1, -1):
            if nums[index] + index >= goal_index:
                # can jump + start point >= goal_index
                goal_index = index
            else:
                continue
        return goal_index == 0
