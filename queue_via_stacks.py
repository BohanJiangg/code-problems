# -*- coding: utf-8 -*-
"""
Created on Sat May 25 16:57:10 2019

CTCI: Problem 3.4 - Queue Via Stacks
Leetcode: Implement Queue using Stacks

Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.



Time Complexity: push, peek, empty all O(1), pop requires O(n) time complexity because we need to pop everything out, take first element, and then push everything back in
Space Complexity: O(n) for pop because we need to store the rest of the stack in another stack temporarily

@author: bohan
"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack =[]
        self.front = None

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        
        if len(self.stack) == 0:
            self.front = x
        self.stack.append(x)        
        
        
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        
        temp = []
        for i in range(len(self.stack)-1):    
            temp.append(self.stack.pop())
        
        toRet = self.stack.pop()
        
        for i in range(-1, -len(temp), -1):
            if i == -1:
                self.front = temp[i]
            self.stack.append(temp[i])
            
        return toRet


        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        
        return self.front
        
        


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()