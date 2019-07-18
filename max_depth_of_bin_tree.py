# -*- coding: utf-8 -*-
"""
Created on July 18 2019
Leetcode: Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.


Time Complexity O(n), goes through all nodes of tree 
Space Complexity: O(1), keeps the depth of node stored. 
@author: bohan
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        def maxRecur(node, depth):
            
            if not node:
                return depth
            depth += 1
            
            leftDepth = rightDepth = 0
            if node.left:
                leftDepth = maxRecur(node.left, depth)
            
            if node.right:
                rightDepth = maxRecur(node.right, depth)

            return max(depth, leftDepth, rightDepth)
        
        return maxRecur(root, 0)