# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 21:07:23 2019
Leetcode: Flatten 2D Vector

Design and implement an iterator to flatten a 2d vector. It should support the following operations: next and hasNext.
Example:

Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // return 1
iterator.next(); // return 2
iterator.next(); // return 3
iterator.hasNext(); // return true
iterator.hasNext(); // return true
iterator.next(); // return 4
iterator.hasNext(); // return false

Notes:

    Please remember to RESET your class variables declared in Vector2D, as static/class variables are persisted across multiple test cases. Please see here for more details.
    You may assume that next() call will always be valid, that is, there will be at least a next element in the 2d vector when next() is called.

Time Complexity: O(n), concatenate 2D list
Space Complexity: O(n), need to store flattened list  

@author: bohan

"""
class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.vector = sum(v, [])

    def next(self):
        """
        :rtype: int
        """
        return self.vector.pop(0)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.vector:
            return True
        else:
            return False


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()