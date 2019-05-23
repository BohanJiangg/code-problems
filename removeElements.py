# -*- coding: utf-8 -*-
"""
Created on May 23 2019
Leetcode: Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.
Time Complexity O(m+n+k) 
Space Complexity: O(k)

@author: bohan
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        