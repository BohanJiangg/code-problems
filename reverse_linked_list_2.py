# -*- coding: utf-8 -*-
"""
Created on May 23 2019
Leetcode: Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Time Complexity O(n), 
Space Complexity: O(1), 
@author: bohan
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        list_head = head
        for i in range(m):
            head = head.next
        
        m_ptr = head
        weaver = head
        weaver2 = head



        
