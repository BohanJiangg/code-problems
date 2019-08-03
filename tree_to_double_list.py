# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 12:58:27 2019
Leetcode: Convert Binary Search Tree to Sorted Doubly Linked List


Time Complexity: O(n), traverse BST once
Space Complexity: O(n), create DLL of same list

@author: bohan

"""
# root of a BST
#    -left, right, val
# head of a doubly linked list (sorted)
# largest.next --> smallest
# smallest.prev --> largest
#
#
# [1] <--> [2] <--> [3] <--> [4] <--> [5] 


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
    
    if not root: return
    
    dummy = Node(0, None, None)
    
    prev = dummy
    
    stack, node = [], root
    
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        node.left, prev.right, prev = prev, node, node
        node = node.right
    
    dummy.right.left, prev.right = prev, dummy.right
    
    return dummy.right
    
