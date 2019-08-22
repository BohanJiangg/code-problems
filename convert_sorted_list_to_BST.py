# -*- coding: utf-8 -*-
"""
Created on August 22 2019
Leetcode: Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

Time Complexity O(n log(n)), recurse for every node in the list, and takes log(n) time to find middle element
Space Complexity: O(log n), log(n) recursion stacks because of depth of BST
@author: bohan
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        # tortoise and hare to get to middle of the list
        # [1,2,3,4,5] slow = 3
        # [1,2,3,4,5,6] slow = 4
        # [1,2]
        # [-10,-3,0,5,9]

        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # tmp points to root
        tmp = slow.next
        # cut down the left child
        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        
        return root







