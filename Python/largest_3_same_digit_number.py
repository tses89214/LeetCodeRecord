"""
You are given a string num representing a large integer. 
An integer is good if it meets the following conditions:
It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:
A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.
 
Example 1:
Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".

Example 2:
Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.

Example 3:
Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.
"""


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        """
        Step:
            1. for loop from first digit to last digit.
            2. keep the digit, and compare to the next digit,
                if meet 3 times continuously,
                keep it as a candidate.
            3. compare the new candidate and old candidate
                and replace it when new one is larger.  
        """
        keep = ""
        count = 0
        candidates = ""
        for digit in num:
            if digit != keep:
                keep = digit
                count = 1
            else:
                count += 1

                if count == 3:
                    new_candidates = f"{digit}{digit}{digit}"
                    if new_candidates > candidates:
                        candidates = new_candidates
                        count == 0

        return candidates
