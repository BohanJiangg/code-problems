# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:47:34 2019

Leetcode: Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6



Time Complexity: O(n), preorder traversal of Binary tree
Space Complexity: O(1), just need to count num nodes


@author: bohan
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        self.cnt = 0
        
        def traverse(node):
            if not node:
                return
            else:
                self.cnt += 1
                traverse(node.left)
                traverse(node.right)
        
        traverse(root)
        return self.cnt