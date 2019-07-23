# -*- coding: utf-8 -*-
"""
Created on July 23 2019
Leetcode: K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Time Complexity O(n log n), need to sort the distances for all the points 
Space Complexity: O(n), need to store a dictionary of distance:index to map the points 
@author: bohan
"""

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if not K:
            return []
        
        distances = {}

        for i in range(len(points)):
            point = points[i]
            dist = point[0] ** 2 + point[1] **2
            if dist in distances:
                distances[dist].append(i)
            else:
                distances[dist] = [i]
        
        
        closest = sorted(distances.keys())

        toRet = []

        i = 0
        while i < K:
            pointsList = distances[closest[i]]
            while pointsList and i < K:
                toRet.append( points[pointsList.pop(0)] )
                i+=1
            
  
        return toRet 


        
