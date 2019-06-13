# -*- coding: utf-8 -*-
"""
Created on June 13 2019
Leetcode: LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

Time Complexity O(n), in the worst case, need to search through entire lru_q list to find value to remove 
Space Complexity: O(2n) needs a dict to store (key,value) pairs as well as a list of keys to track LRU cache 
@author: bohan
"""

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.lru_q = []
        self.capacity = capacity
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        if key in self.cache:
            
            self.lru_q.remove(key)
            self.lru_q.append(key)
            
            return self.cache[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.lru_q.remove(key)
            self.lru_q.append(key)
            self.cache[key] = value

        elif len(self.cache) < self.capacity:
            # Smaller than capacity
            self.cache[key] = value
            self.lru_q.append(key)
        else:
            to_del = self.lru_q.pop(0)
            
            del self.cache[to_del]
            self.cache[key] = value
            self.lru_q.append(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


