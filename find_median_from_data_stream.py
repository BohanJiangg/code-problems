# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 08:45:41 2019
Leetcode: Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
For example,

[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

    void addNum(int num) - Add a integer number from the data stream to the data structure.
    double findMedian() - Return the median of all elements so far.


Time Complexity O(log n), heap insertion time
Space Complexity: O(n), linear space to hold two containers 
@author: bohan
"""

# Note that items in small are negated 
# large[0] contains the median element, and also is a min heap of the largest most elements
# Small is a min heap of the negative values of the smaller elements
from heapq import *
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [], []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))
        

    def findMedian(self):
        """
        :rtype: float
        """
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        
        return (large[0] - small[0])/2.0
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Below solution too slow with O(n) insertion time
#    def __init__(self):
#        """
#        initialize your data structure here.
#        """
#        self.storage = []
#        
#
#    def addNum(self, num):
#        """
#        :type num: int
#        :rtype: None
#        """
#        
#        length = len(self.storage)
#        for i in range(length):
#            if self.storage[i] > num:
#                self.storage.insert(i, num)
#                break
#            elif i == length -1:
#                self.storage.insert(i+1, num)
#                break
#
#        
#        if not self.storage:
#            self.storage.append(num)
#        
#                            
#        
#
#    def findMedian(self):
#        """
#        :rtype: float
#        """
#        if not self.storage:
#            return -1
#        
#        length = len(self.storage)
#        if length % 2 == 1:
#            return float(self.storage[int(length/2)])
#        else:
#            return (self.storage[int(length/2) -1] + self.storage[int(length/2)])/float(2) 
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()