# -*- coding: utf-8 -*-
"""
Created on May 23 2019
Leetcode: Odd Even Linked List
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Time Complexity O(n), need to iterate through the linked list only once (or O(n/2) times)
Space Complexity: O(1), constant number of extra pointers needed
@author: bohan
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return None
        if not head.next:
            return head

        toRet = head
        odd_ptr = head
        even_ptr = head.next
        even_ptr_head = even_ptr
        
        while even_ptr and even_ptr.next and odd_ptr.next.next:
            odd_ptr.next = odd_ptr.next.next
            even_ptr.next = even_ptr.next.next

            odd_ptr = odd_ptr.next
            even_ptr = even_ptr.next
            
        odd_ptr.next = even_ptr_head

        return toRet
            



