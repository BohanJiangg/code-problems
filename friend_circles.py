# -*- coding: utf-8 -*-
"""
Created on June 14 2019
Leetcode: Friend Circles

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.


Time Complexity O(N^2), since need to traverse every node in the matrix 
Space Complexity: O(N), for visited list of length N
@author: bohan
"""

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        
        ppl = len(M)
        
        visited = []
        res = 0
        
        def dfs(node):
            for idx, value in enumerate(M[node]):
                if value and not idx in visited:
                    visited.append(idx)
                    dfs(idx)
                    
        for i in range(ppl):
            if not i in visited:
                visited.append(i)
                dfs(i)
                res += 1
        return res


