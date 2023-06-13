"""
https://leetcode.com/problems/search-a-2d-matrix/?envType=study-plan-v2&envId=top-interview-150
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans_i = 0

        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        for i in range(1, len(matrix)):
            if target > matrix[i][0]:
                ans_i = i
            elif target == matrix[i][0]:
                return True
            else:
                break

        for j in range(len(matrix[ans_i])):
            m = matrix[ans_i][j]
            if target == m:
                return True
            elif target < m:
                return False
