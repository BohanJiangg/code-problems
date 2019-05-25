# -*- coding: utf-8 -*-
"""
Created on Sat May 25 15:17:19 2019


CTCI: Problem 2.5 - Sum Lists
Leetcode: Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


Time Complexity: O(max(m,n)), since we iterate through both numbers at the same time and then do another iteration of the same magnitude to create the linked list 
Space Complexity: O(max(m,n)), need a list of numbers to keep track of sum as we iterate through the lists. 

@author: bohan
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        sum_list = []
        temp = 0
        
        while l1 and l2:
            sum_list.append( (temp + l1.val + l2.val) % 10)
            temp = (temp + l1.val + l2.val)/10
            
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            sum_list.append((temp+l1.val)%10)
            temp = (temp+l1.val)/10
            
            l1 = l1.next
            
        while l2:
            sum_list.append((temp+l2.val)%10)
            temp = (temp+l2.val)/10
            
            l2 = l2.next
        
        if temp:
            sum_list.append(temp)
        
        head = toRet = ListNode(sum_list[0])
        
        for i in range(1, len(sum_list)):
            head.next = ListNode(sum_list[i])
            head = head.next
    
        
        return toRet
            
            
            
            
            
            
            
            
            
            
            
            