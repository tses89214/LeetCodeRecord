"""
https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150
Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.


Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        1. convert magazine to a list (every alphabet).
        2. remove from magazine list one by one according to ransomNote.
        3. skip when meet ValueError.
        """
        magazine_list = list(magazine)
        for word in ransomNote:
            try:
                magazine_list.remove(word)
            except ValueError:
                return False
        return True
