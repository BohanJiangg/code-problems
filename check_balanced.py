# -*- coding: utf-8 -*-
"""
Created on Sun May 26 15:29:05 2019


CTCI: Problem 4.4 - Check Balanced
Leetcode: Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
    a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Given the following tree [3,9,20,null,null,15,7]:
    
    
Time Complexity: O(n), worst case go through all subtrees to check for balance  
Space Complexity: O(h), (h is the height of the tree), h recursive calls needed to explore entire tree if very unbalanced.

@author: bohan
"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
        
        if not root.left and not root.right:
            return True
        
        leftLvl = self.balancedHelper(root.left, 1)
        if leftLvl == False:
            return False
        rightLvl = self.balancedHelper(root.right, 1)
        if rightLvl == False:
            return False
        
        
        if abs(leftLvl - rightLvl) > 1:
            return False
        return True
        
        
    
    def balancedHelper(self, node, lvl):
        
        if not node:
            return lvl
        
        leftLvl = rightLvl = lvl + 1
        
        
        if node.left:    
            leftLvl = self.balancedHelper(node.left, lvl+1)
            if leftLvl == False:
                return False
        if node.right:
            rightLvl = self.balancedHelper(node.right, lvl+1)
            if rightLvl == False:
                return False
            
        if abs(leftLvl - rightLvl) > 1:
            return False
        else:
            return max(leftLvl, rightLvl)
        
        
        
        
        
        
        