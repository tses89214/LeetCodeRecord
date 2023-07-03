"""
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/?envType=study-plan-v2&envId=top-interview-150

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 
Constraints:
1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Keep a list length is K,
        and replace it when find larger number.
        The last one element is the answer.

        brute force:
            target_list = [float('-inf')] * k
            smallest = target_list[-1]
            for element in nums:
                if element > smallest:
                    for index, target_ele in enumerate(target_list):
                        if element > target_ele:
                            target_list[index+1:] = target_list[index:k-1]
                            target_list[index] = element
                            break
            return target_list[-1]
        """
        from heapq import heappop, heappush
        target_list = []
        count = 0
        for ele in nums:
            heappush(target_list, ele)
            count += 1
            if count > k:
                heappop(target_list)
                count -= 1
        return target_list[0]
