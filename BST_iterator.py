# -*- coding: utf-8 -*-
"""
Created on August 7 2019    
Leetcode: Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Example:
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
 
Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

Time Complexity O(n), need to parse through BST at initialization, next() and hasNext O(1)
Space Complexity: O(n), stores BST inorder in a list 
@author: bohan
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # Need to parse the tree inorder
        self.list = []

        def parse(node):
            if not node:
                return
            else:
                parse(node.left)
                self.list.append(node.val)
                parse(node.right)
        
        parse(root)
        

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self.list.pop(0)
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return True if self.list else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()