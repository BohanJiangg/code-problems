# -*- coding: utf-8 -*-
"""
Created on August 21 2019
Leetcode: Exclusive Time of Functions

On a single threaded CPU, we execute some functions.  Each function has a unique id between 0 and N-1.

We store logs in timestamp order that describe when a function is entered or exited.

Each log is a string with this format: "{function_id}:{"start" | "end"}:{timestamp}".  For example, "0:start:3" means the function with id 0 started at the beginning of timestamp 3.  "1:end:2" means the function with id 1 ended at the end of timestamp 2.

A function's exclusive time is the number of units of time spent in this function.  Note that this does not include any recursive calls to child functions.

The CPU is single threaded which means that only one function is being executed at a given time unit.

Return the exclusive time of each function, sorted by their function id.

Input:
n = 2
logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3, 4]
Explanation:
Function 0 starts at the beginning of time 0, then it executes 2 units of time and reaches the end of time 1.
Now function 1 starts at the beginning of time 2, executes 4 units of time and ends at time 5.
Function 0 is running again at the beginning of time 6, and also ends at the end of time 6, thus executing for 1 unit of time. 
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.

Time Complexity O(n), 
Space Complexity: O(1), 
@author: bohan
"""

class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        
        if n == 0:
            return []
        toRet = [0] * n
        '''
        2
        ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
        [7,1]
        [[0,0,2],[]]
        '''
        stack = []
        first = logs[0].split(':')
        stack.append( [int(first[0]), int(first[2])] )
        currTime = int(first[2])
        for item in logs[1:]:
            item = item.split(':')
            if item[1] == 'start':
                currTime = int(item[2])
                if stack:
                    stack[-1].append(currTime - stack[-1][1])
                stack.append([int(item[0]), currTime])
            else:
                res = stack.pop(-1)
                if len(res) == 3:
                    toRet[res[0]] = res[2] + (int(item[2]) - currTime)
                else:
                    toRet[res[0]] = (int(item[2]) - res[1])+1
                currTime = int(item[2])

        return toRet  