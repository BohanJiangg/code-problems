# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 11:37:47 2018
Leetcode: Merge Two Sorted Lists
Time Complexity: O(m+n) where m is length of l1, n is length of l2
Space Complexity: O(1), since the function simply rearranges the order of the list nodes.
@author: bohan
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        l1Done = False
        l2Done = False
        
        if l1.val < l2.val:
            res = l1
            if l1.next:
                l1 = l1.next
            else:
                l1Done = True
        else:
            res = l2
            if l2.next:
                l2 = l2.next
            else:
                l2Done = True
                
        resHead = res
        
        while l1 != None or l2 != None:

            if l1Done == False and l2Done == False:
                if l1.val < l2.val:
                    res.next = l1
                    
                    if l1.next == None:
                        l1Done = True
                    else:
                        l1 = l1.next
                
                else:
                    res.next = l2
                    if l2.next == None:
                        l2Done = True
                    else:
                        l2 = l2.next
            
            elif l1Done == True and l2Done == True:
                break
                
            elif l1Done == True:
                res.next = l2
                if l2.next == None:
                    l2Done = True
                else:
                    l2 = l2.next
            
            elif l2Done == True:
                res.next = l1
                if l1.next == None:
                    l1Done = True
                else:
                    l1 = l1.next
            
            res = res.next

        return resHead