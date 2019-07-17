# -*- coding: utf-8 -*-
"""
Created on July 17 2019
Leetcode: Course Schedule

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.


Time Complexity O(V+E), in worse case where there are no cycles 
Space Complexity: O(V), need graph and visited list to keep track of all edges and visited nodes 
@author: bohan
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True
        
        graph = [[] for i in range(numCourses)]
        visited = [0 for i in range(numCourses)]

        for item in prerequisites:
            graph[item[0]].append(item[1])
        
        def dfs(course):
            if visited[course] == 1:
                return True
            if visited[course] == -1:
                return False
            
            visited[course] = -1

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            visited[course] = 1
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True


        
    
        
        
        
        
    



        