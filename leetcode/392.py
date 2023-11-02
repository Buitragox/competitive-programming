# 02/11/2023 dd/mm/yyyy
# Jhoan Buitrago
# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """Given two strings s and t, return true if s is a subsequence of t, or false otherwise."""
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False

        i = 0
        for letter in t:              
            if s[i] == letter:
                i += 1
                if i == len(s):
                    break  

        return (i == len(s))


if __name__ == "__main__":
    s = "ahc"
    t = "ahbgdc"

    print(Solution().isSubsequence(s, t))