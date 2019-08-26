# -*- coding: utf-8 -*-
"""
Created on August 26 2019
Leetcode: Find Leaves of Binary Tree

Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Example:

Input: [1,2,3,4,5]
  
          1
         / \
        2   3
       / \     
      4   5    

Output: [[4,5,3],[2],[1]]

Time Complexity O(n), go through binary tree once
Space Complexity: O(n), store all nodes in a list
@author: bohan
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
          
        leaves = collections.defaultdict(list)
        def rec(node, level):
            if not node:
                return 0 
            else:
                left = rec(node.left, level+1)
                right = rec(node.right, level+1)
                level = max(left, right) + 1
                leaves[level].append(node.val)
                return level
        

        rec(root, 0)
        maxLevels = max(leaves.keys())
        toRet = []

        for i in range(1,maxLevels+1):
            toRet.append(leaves[i])

        return toRet
