# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 19:44:49 2019
Leetcode: Network Delay Time

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2

Time Complexity O(n), 
Space Complexity: O(1), 
@author: bohan
"""

class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        
        if N == 1:
            return 0
        # make adj matrix
        graph = [[] for i in range(N+1)]
        
        for item in times:
            graph[item[0]].append((item[2], item[1]))
         
        dist = {node: float('inf') for node in range(1, N+1)}
        
        def dfs(node, elapsed):
            if dist[node] < elapsed: 
                return
    
            dist[node] = elapsed
            
            for item in sorted(graph[node]):
                dfs(item[1], elapsed + item[0])
        
        dfs(K, 0)
        ans = max(dist.values())
        if ans < float('inf'):
            return ans
        else:
            return -1
            
            
     
        
        
        
        
        
        