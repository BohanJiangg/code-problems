# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 20:16:29 2019
Leetcode: High Five

Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.

Time Complexity: O(k (n log n)), need to sort scores for every student k
Space Complexity: O(n), need to set up dict and return list 

@author: bohan

"""

class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
    
        studentList = {}
        for i in items:
            if not i[0] in studentList:
                studentList[i[0]] = [i[1]]
            else:
                studentList[i[0]].append(i[1])
        
        toRet = []
        for id, scores in studentList.items():
            toRet.append([id, sum(sorted(scores)[:5])/5])
        
        return toRet
        
        
        
        
        
        
        
        
        
        