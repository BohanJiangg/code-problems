# -*- coding: utf-8 -*-
"""
Created on Sun May 26 16:09:26 2019


CTCI: Problem 4.5 - Validate BST
Leetcode: Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

    
Time Complexity: O(n), since we traverse tree only once
Space Complexity: O(n), since we keep up to entire tree

@author: bohan
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.checkBST(root)
        
        
    def checkBST(self, root, minVal = float('-inf'), maxVal = float('inf')):
        if root == None:
            return True
        
        val = root.val
        if val <= minVal or val >= maxVal:
            return False
        
        if not self.checkBST(root.left, minVal, val):
            return False
        if not self.checkBST(root.right, val, maxVal):
            return False
        return True
        
       
       