# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:27:48 2019

CTCI: Problem 4.8 - First Common Ancestor
Leetcode: Lowest Common Ancestor of a Binary Tree
Time Complexity: O(n), iterate through all nodes of the tree at most twice (second time to get ancestors)
Space Complexity: O(n), need to keep track of ancestors

@author: bohan

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        stack = [root]
        
        parents = {root: None}
        
        while not p in parents or not q in parents:
            curr = stack.pop()
            if curr.left:
                stack.append(curr.left)
                parents[curr.left] = curr
            if curr.right:
                stack.append(curr.right)
                parents[curr.right] = curr
        
        ancestors = set()
        
        while p:
            ancestors.add(p)
            p = parents[p]
        
        while not q in ancestors:
            q = parents[q]
        return q
        
        
        
        
        
            
    
        
        