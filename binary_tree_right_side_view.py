# -*- coding: utf-8 -*-
"""
Created on August 2 2019
Leetcode: 

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]

Time Complexity O(n), traverse all nodes once 
Space Complexity: O(depth(n)), only take one node (right side node) per depth level  
@author: bohan
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        def collect(node, depth):
            if node:
                if len(view) == depth:
                    view.append(node.val)
                collect(node.right, depth+1)
                collect(node.left, depth+1)

        view = []
        collect(root, 0)
        return view 