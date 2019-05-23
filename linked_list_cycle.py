# -*- coding: utf-8 -*-
"""
Created on May 23 2019
Leetcode: Linked List Cycle
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
Time Complexity O(n), in the worst case, we iterate through the linked list once
Space Complexity: O(1), only need two ptrs in both cases
@author: bohan
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        

        # Return false if no node or single node
        if not head or not head.next:
            return False
        
        fast_ptr = head
        while fast_ptr.next and fast_ptr.next.next:
           head = head.next
           fast_ptr = fast_ptr.next.next
           if head == fast_ptr:
               return True

        return False
