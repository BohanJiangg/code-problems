# -*- coding: utf-8 -*-
"""
Created on May 23 2019
Leetcode: Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.
Time Complexity O(n), iterate through the linked list once
Space Complexity: O(1), need two pointers toRet and target

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
        
        # Find first node head where head.val != val
        while head and head.val == val:
            head = head.next
        
        if not head:
            return head

        # toRet is first head node != val    
        toRet = head    

        # Check for subsequent nodes that are equal to val
        while head and head.next:
            if head.next.val == val:
                target = head.next
                while target.val == val and target.next:
                    target = target.next
                # either reached a node that != val or target has no next
                # or reached a node that != val AND has no next
                if (not target.next) and target.val != val:
                    head.next = target
                    return toRet
                elif target.next: 
                    head.next = target
                else:
                    head.next = None
                    return toRet
            
            head = head.next
        

        return toRet
