# -*- coding: utf-8 -*-
"""
Created on August 31 2019
Leetcode: All Paths From Source to Target

Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.


Time Complexity: O(2^n), 2*n possible paths (appearing or not appearing in path)
Space Complexity: O(2^n * N), total number of possible paths times length of each path 

@author: bohan

"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        if not graph: 
            return []

        if len(graph) == 1:
            return [[0]]
        
        target = len(graph) - 1

        toRet = set()

        def rec(node, path):
            if node == target:
                toRet.add(path)
                return
            else:
                for i in graph[node]:
                    temp = path + (i,)
                    rec(i, temp)
        
        rec(0, (0,))

        toRet = list(toRet)
        toRet = [list(x) for x in toRet]
        return toRet

            

        