# -*- coding: utf-8 -*-
"""
Created on July 11 2019
Leetcode: Design HashMap

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

Example:

MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);          // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);          // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 

Note:

All keys and values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashMap library.


Time Complexity O(1) average case, O(n) worst case 
Space Complexity: O(n) with list of lists
@author: bohan
"""

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 1000
        self.list = [None]*self.m

        
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        hash = key % self.m
        
        if not self.list[hash]:
            self.list[hash] = [[key,value]]
            return None
        else:
            idx = 0
            limit = len(self.list[hash])
            lis = self.list[hash]
            ptr = self.list[hash]
            while idx < limit:
                ptr = lis[idx]
                if ptr[0] == key:
                    ptr[1] = value
                    return None
                idx += 1
            self.list[hash].append([key, value])
            return None

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hash = key % self.m
        if not self.list[hash]:
            return -1
        else:
            idx = 0
            limit = len(self.list[hash])
            lis = self.list[hash]
        
            ptr = self.list[hash]
            while idx < limit:
                ptr = lis[idx]
                if ptr[0] == key:
                    return ptr[1]
                idx += 1
            
        return -1

        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hash = key % self.m
        if not self.list[hash]:
            return None
        else:
            idx = 0
            limit = len(self.list[hash])
            lis = self.list[hash]
            ptr = self.list[hash]
            while idx < limit:
                ptr = lis[idx]
                if ptr[0] == key:
                    del lis[idx]
                    return None
                idx += 1
            
        return None


        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
