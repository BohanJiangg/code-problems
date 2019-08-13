# -*- coding: utf-8 -*-
"""
Created on August 13 2019  
Leetcode: Number of Islands II

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0


Union Find
is an abstract data structure supporting find and unite on disjointed sets of objects, typically used to solve the network connectivity problem.

The two operations are defined like this:

find(a,b) : are a and b belong to the same set?

unite(a,b) : if a and b are not in the same set, unite the sets they belong to.

With this data structure, it is very fast for solving our problem. Every position is an new land, if the new land connect two islands a and b, we combine them to form a whole. The answer is then the number of the disjointed sets.

Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?

Time Complexity O(n log n), but O(mn) for array initialization
Space Complexity: O(mn), need to create the graph  
@author: bohan
"""

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        
        ans = []
        islands = Union()
        for p in map(tuple, positions):
            if p in islands.id:
                ans += [islands.count]
                continue
            islands.add(p)
            # Iterate through 4 adjacent positons
            for dp in (0, 1), (0, -1), (1, 0), (-1, 0):
                # each q is an adjacent spot
                q = (p[0] + dp[0], p[1] + dp[1])
                # if q is in dict of islands
                if q in islands.id:
                    islands.unite(p, q)
            # add current count to list
            ans += [islands.count]
        return ans

class Union(object):
    def __init__(self):
        self.id = {}
        self.sz = {}
        self.count = 0

    def add(self, p):
        self.id[p] = p
        self.sz[p] = 1
        self.count += 1

    def root(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def unite(self, p, q):
        i, j = self.root(p), self.root(q)
        if i == j:
            return
        if self.sz[i] > self.sz[j]:
            i, j = j, i
        self.id[i] = j
        self.sz[j] += self.sz[i]
        self.count -= 1
