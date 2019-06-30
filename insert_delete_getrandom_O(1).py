# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 14:50:22 2019

Leetcode: Insert Delete GetRandom O(1)

Design a data structure that supports all following operations in average O(1) time.

    insert(val): Inserts an item val to the set if not already present.
    remove(val): Removes an item val from the set if present.
    getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

Time Complexity: O(1), as per specification. val in dict is average O(1) time.
Space Complexity: O(n), one dict and one list per value 

@author: bohan

"""

import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict, self.vals = {}, []

       

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        
        
        
        if not val in self.dict:
            self.vals.append(val)
            self.dict[val] = len(self.vals) - 1
            return True
        return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        
        
        
        if not val in self.dict:
            return False
        else:    
            
            if val == self.vals[-1]:
                del self.dict[val]
                self.vals.pop(-1)
            else:
                idx = self.dict[val]
                lastVal = self.vals[-1]
                self.vals.pop(-1)
                self.vals[idx] = lastVal
                del self.dict[val]
                self.dict[lastVal] = idx
            
            return True



    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
       
        return self.vals[random.randint(0, len(self.vals) - 1)]



'''
Solution below using O(n) time due to requiring dict.items()
import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

       

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        
        if val in self.dict:
            return False
        else:
            self.dict[val] = val
            return True
        
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        
        if not val in self.dict:
            return False
        else:    
            del self.dict[val]
 
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        lis = self.dict.items()
        
        return lis[random.randint(0, len(self.dict) - 1)][0]
        
'''        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()