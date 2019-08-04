
"""
Created on Sun Aug  4 13:50:41 2019
Leetcode: One Edit Distance

Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

    Insert a character into s to get t
    Delete a character from s to get t
    Replace a character of s to get t

Time Complexity: O(n), one-pass
Space Complexity: O(n), convert string to list  

@author: bohan

"""

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if not s and not t:
            return False
    
        if abs(len(s) - len(t)) == 1:
            if len(s) > len(t):
                for i in range(len(t)):
                    if s[i] != t[i]:
                        if not s[:i] + s[i+1:] == t:
                            return False
                        else:
                            return True
                return True

            else:
                for i in range(len(s)):
                    if s[i] != t[i]:
                        if not t[:i] + t[i+1:] == s:
                            return False
                        else:
                            return True
                return True

        elif len(s) == len(t):
            # replacement
            s_list = list(s)
            for i in range(len(s_list)):
                if s_list[i] != t[i]:
                    s_list[i] = t[i]
                    if ''.join(s_list) == t:
                        return True
                    else:
                        return False

        else:
               return False