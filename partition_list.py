# -*- coding: utf-8 -*-
"""
Created on Sat May 25 14:26:00 2019

CTCI: Problem 2.4 - Partition
Leetcode: Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Time Complexity: O(n), iterate through list once
Space Complexity: O(1), only a few pointers needed  

@author: bohan
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        
        smallStart = smallHead = ListNode(None)
        largeStart = largeHead = ListNode(None)
    
        
        while head:
            if head.val < x:
                smallHead.next = head
                smallHead = smallHead.next
            else:
                largeHead.next = head
                largeHead = largeHead.next
            head = head.next
            
        largeHead.next = None
        smallHead.next = largeStart.next
        
        return smallStart.next
        
    
        
        
        
        
        
        
        