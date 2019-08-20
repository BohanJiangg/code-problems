# -*- coding: utf-8 -*-
"""
Created on August 20 2019
Leetcode: Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

Time Complexity O(n), one-pass solution
Space Complexity: O(n), keep track of references in list 
@author: bohan
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        

        toRet = head
        refs = []
        while head:
            refs.append(head)
            head = head.next
        
        if (n-1 == 0):
            prev = refs[-(n+1)]
            prev.next = None
            return toRet
        elif (n+1 > len(refs)):
            toRet = toRet.next
            return toRet
        else: 
            prev = refs[-(n+1)]
            nxt = refs[-(n-1)]
            
            prev.next = nxt

            return toRet