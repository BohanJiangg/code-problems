# -*- coding: utf-8 -*-
"""
Created on September 6 2019
Leetcode: Fizz Buzz

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]


Time Complexity: O(n), go through nums 1 to n
Space Complexity: O(n), need to store all nums in array to return 

@author: bohan

"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        if not n or n <= 0:
            return []

        toRet = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                toRet.append('FizzBuzz')
            elif i % 3 == 0:
                toRet.append("Fizz")
            elif i % 5 == 0:
                toRet.append('Buzz')
            else:
                toRet.append(str(i))
        return toRet
        

        