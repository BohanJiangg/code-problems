# -*- coding: utf-8 -*-
"""
Created on May 23 2019
Leetcode: Remove Duplicates from Sorted List
Given a sorted linked list, delete all duplicates such that each element appear only once.

Unsorted list: 
Time Complexity: O(n^2), in the worst case where there are no duplicates, we have to iterate through the linked list, and at each iteration the in operator is used to search through the dup_list
Space Complexity: O(n), the worst case occurs when there are no duplicates


Sorted list:
Time Complexity: O(n), iterate through the linked list once, all duplicate nodes are skipped over
Space Complexity: O(1), only need two pointers (toRet and target) for the problem

@author: bohan
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        The below code deals with unsorted lists!
        :type head: ListNode
        :rtype: ListNode
        """
        
        dup_list = []

        if not head:
            return head
        
        toRet = head
        dup_list.append(head.val)

        while head and head.next:
            if head.next.val in dup_list:
                target = head.next
                while target.next and target.next.val in dup_list:
                    target = target.next
                
                # two options here, target.next doesn't exist or target.next.val not a duplicate

                if target.next:
                    head.next = target.next
                else:
                    head.next = None
                    return toRet
            dup_list.append(head.next.val)
            head = head.next        


        return toRet

    def deleteDuplicates1(self, head):
        """
        The below code deals with sorted lists
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head
        
        toRet = head

        while head and head.next:
            if head.val == head.next.val:

                target = head.next
                while target.next and target.next.val == head.val:
                    target = target.next
                
                # two options here, target.next doesn't exist or target.next.val not a duplicate

                if target.next:
                    head.next = target.next
                else:
                    head.next = None
                    return toRet
            
            head = head.next        


        return toRet
        