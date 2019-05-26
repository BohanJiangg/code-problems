# -*- coding: utf-8 -*-
"""
Created on Sat May 25 16:39:41 2019


CTCI: Problem 3.2 - Stack Min
Leetcode: Min Stack

 Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.


Time Complexity: O(n) in the worst case in pop() when the next minimum element has to be identified
Space Complexity: O(n), length of the stack

To get O(1) time complexity, use a second stack that keeps track of the minimums at that point in the stack (if < current min, push in stack)

@author: bohan
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minElement = None
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        
        if x < self.minElement or self.minElement == None:
            self.minElement = x
        self.stack.append(x)
        
        
    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            toRet = self.stack.pop()
            if toRet == self.minElement:
                if self.stack:
                    self.minElement = min(self.stack)
                else:
                    self.minElement = None
            return toRet
        else:
            return None

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        
        return self.minElement
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()