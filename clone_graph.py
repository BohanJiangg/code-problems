# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 21:19:42 2019
Leetcode: Clone Graph

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

Time Complexity: O(V+E), iterate through all nodes and edges in the graph
Space Complexity: O(V+E), need to clone the graph 

@author: bohan

"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visited = {}
        def cloneHelper(node):
            if node and not node in visited:
                newNode = Node(node.val, None)
                visited[newNode.val] = newNode
                newNode.neighbors = [visited.get(n.val) or cloneHelper(n) for n in node.neighbors]
                return newNode
        return cloneHelper(node)
        
        
        
        