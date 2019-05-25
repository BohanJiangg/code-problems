# -*- coding: utf-8 -*-
"""
Created on Sat May 25 15:49:47 2019


CTCI: Problem 2.6 - Palindrome
Leetcode: Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.


Time Complexity: O(n), iteration over linked list and then O(n/2) for list
Space Complexity: O(n), need a list to store the values

@author: bohan
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or not head.next:
            return True
        
        
        # Using a list for O(n) space:
        lis = []
        
        while head:
            lis.append(head.val)
            head = head.next
        
        for i in range(len(lis)/2):
            if lis[-i-1] != lis[i]:
                return False
        return True
        
        
        

