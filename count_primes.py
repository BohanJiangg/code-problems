# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 17:24:38 2019
Leetcode: Count Primes

Count the number of prime numbers less than a non-negative number, n.

Time Complexity O(n log log n), Sieve of Eratosthenes algorithm
Space Complexity: O(n), keep track of all Primes 
@author: bohan
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        isPrime = [True] * n
        
        
        for i in range(2, int(n**(0.5)) +1):
            if not isPrime[i]:
                continue
            
            for j in range(i*i, n, i):
                isPrime[j] = False
        
        count = 0
        
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        
        
        return count