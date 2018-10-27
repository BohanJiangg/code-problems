# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 10:20:00 2018
Leetcode: Reverse Words in a String

Time Complexity: O(n) time
Space complexity: O(n) space

@author: bohan
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s.strip(' ') == '':
            return ''
        
        listWords = s.split(" ")
        for word in listWords:
            word.strip(' ')

        listWords = [x for x in listWords if x != '']
                
                
        result = ''
        for i in range(len(listWords) - 1, -1, -1):
                if i == 0:
                    result = result + listWords[i]
                else:
                    result = result + listWords[i] + ' '
        
        

        return result