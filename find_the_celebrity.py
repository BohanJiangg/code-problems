# -*- coding: utf-8 -*-
"""
Created on August 21 2019
Leetcode: Find the Celebrity

Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

Time Complexity O(n), go through n multiple times
Space Complexity: O(1), only need to keep track of one candidate
@author: bohan
"""

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        
        # Initialize target candidate to be first 
        target = 0
        for i in xrange(n):
            # if candidate knows anyone, they can't be the celebrity
            # Switch target
            if knows(target, i):
                target = i
        
        # Confirm that target doesnt know anyone up to him
        if any(knows(target, i) for i in xrange(target)):
            return -1
        # Confirm that no one doesn't know target
        if any(not knows(i, target) for i in xrange(n)):
            return -1
        return target
       