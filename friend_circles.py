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


Time Complexity O(n), 
Space Complexity: O(1),
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
        
        fCircles = len(M)
        toVisit = {}
        visitQ = []
        fGroups = {}

        for i in range(fCircles):
            fGroups[i] = [i]

        for i in range(fCircles-1):
            for j in range(i+1, fCircles):
                toVisit[(j,i)] = M[j][i]
                visitQ.append((j,i))
            
        
        print(visitQ)
    
        while visitQ:
            index = visitQ.pop()
            i = index[0]
            j = index[1]
            if (i,j) in toVisit and M[i][j] == 1:
                fCircles -= 1
                if len(fGroups[j]) > 1:
                    for person in fGroups[j]:
                        if person > j and (person,i) in toVisit:
                            del toVisit[(person, i)]

                fGroups[j].append(i) 
        return fCircles


[(1, 0), (2, 0), (3, 0), (4, 0), (2, 1), (3, 1), (4, 1), (3, 2), (4, 2), (4, 3)]            
        