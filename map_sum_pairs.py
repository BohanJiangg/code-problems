# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:15:24 2019
Leetcode: Map Sum Pairs

 Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix. 

Time Complexity O(K) for insert, where K is the length of the key. O(K) for sum as well.
Space Complexity: O(N), linearly with the number of different words stored in the trie. 
@author: bohan
"""


class TrieNode(object):
    __slots__ = 'children', 'score'
    
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.map = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        curr = self.root
        curr.score += delta
        for ch in key:
            curr = curr.children.setdefault(ch, TrieNode())
            curr.score += delta

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        
        curr = self.root
        for ch in prefix:
            if not ch in curr.children:
                return 0
            curr = curr.children[ch]
        
        return curr.score
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)