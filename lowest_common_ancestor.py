# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:27:48 2019

CTCI: Problem 4.8 - First Common Ancestor
Leetcode: Lowest Common Ancestor of a Binary Tree
Time Complexity: O(n),
Space Complexity: O(n),  

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
        
        
        pQueue  = [root]
        qQueue  = [root]
        pVisited = []
        qVisited = []
        
        while pQueue:
            print(pQueue)
            curr = pQueue.pop()
            pVisited.append(curr.val)
            if curr.val == p.val:
                break
            else:
                if curr.left:
                    pQueue.append(curr.left)
                if curr.right:
                    pQueue.append(curr.right)
        
        while qQueue:
            curr = qQueue.pop()
            qVisited.append(curr.val)
            if curr.val == q.val:
                break
            else:
                if curr.left:
                    qQueue.append(curr.left)
                if curr.right:
                    qQueue.append(curr.right)
        
    
        
        if pVisited[-1] == p.val and qVisited[-1] == q.val:
            print(pVisited)
            print(qVisited)
            
    
        
        