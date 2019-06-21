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
        
        toret = head
        if m == n:
            return toret

        stack = [] 
        count = 1 

        # Find ListNode right before node m
        while head.next and count < m-1:
            count += 1
            head = head.next

        startPtr = head 

        while count != n:
            head = head.next
            stack.append(head)
            count += 1
        
        if m == 1:
            if n == 2:
                toret = head
                toret.next = startPtr
                startPtr.next = head.next
                return toret
            startPtr = toret = head
        
        endPtr = head.next

        while not len(stack) == 0:
            startPtr.next = stack.pop()
            startPtr = startPtr.next
        
        startPtr.next = endPtr

        return toret



        
