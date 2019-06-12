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

    
Time Complexity: O(n), 
Space Complexity: O(n), 

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
        if root == None:
            return True
        if not root.left and not root.right:
            return True
        
        leftValid = self.checkBST(root.left, root.val, True, None)
        rightValid = self.checkBST(root.right, root.val, False, None)
        
        return leftValid and rightValid
    

    def checkBST(root, parentMin, parentMax):
        if root == None:
            return True
        
        leftValid = self.checkBST(root.left, min(root.val, parentMin), max(root.val, parentMax))
        rightValid = self.checkBST(root.right, min(root.val, parentMin), max(root.val, parentMax))
        if not leftValid or not rightValid:
            return False
        
        if not (root.right > root.val and root.right < parentMin):
            return False
        if not(root.left < root.val and root.left > parentMax): 
            return False 
        
        








        




        
    
       
       