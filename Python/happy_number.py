"""
https://leetcode.com/problems/happy-number/?envType=study-plan-v2&envId=top-interview-150
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true

Example 2:
Input: n = 2
Output: false
 
Constraints:
1 <= n <= 231 - 1
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        past_num = set()

        while 1:
            if n == 1:
                return True

            num_list = sorted(list(str(n)))
            num_list_str = ''.join(num_list)
            if num_list_str in past_num:
                return False
            else:
                past_num.add(num_list_str)

            temp_sum = 0
            for num in num_list:
                temp_sum += int(num) ** 2
            n = temp_sum
