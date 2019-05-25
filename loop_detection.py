# -*- coding: utf-8 -*-
"""
Created on Sat May 25 16:08:25 2019


CTCI: Problem 2.8 - Loop Detection
Leetcode: Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Using Visited List
Time Complexity: O(n^2), since in worst case we iterate through whole list and search for a duplicate node every time. 
Space Complexity: O(n), since we need to store the references of the linked list in a list

Using two pointers
Time Complexity: O(n), only need to iterate once through list
Space Complexity: O(1), only need additional pointers

@author: bohan
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        
        if not head or not head.next:
            return None
        
        
        # Visited list
        visited = [head]
        
        while head.next:
            if head.next in visited:
                return head.next
            visited.append(head.next)
            head = head.next
        
        return None
    
    
    def detectCycle2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or not head.next:
            return None
        
        slow = fast = start = head
        isMet = False
        
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                isMet = True
                break
        
        
        if isMet:
            while slow != start:
                slow = slow.next
                start = start.next
            return slow
        
        return None             
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            