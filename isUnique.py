# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 08:48:14 2019

CTCI: Problem 1.1 - Is Unique
Time Complexity: With DS = O(n), No DS = O(n log n), timsort
Space Complexity: With DS = O(n) for set, No DS = O(1), just string

@author: bohan
"""

'''
Algorithm that determines if a string has all unique characters 
'''
def isUnique_ds(string):
    s = set()
    # With Data Structure, Adds all characters into unique set, O(n) time
    for ch in string:
        s.add(ch)
    
    if len(string) > len(s):
        return False
    else:
        return True
    
   
'''
Algorithm that determines if a string has all unique characters  - no other data structures
'''    
def isUnique_nods(string):
    # Assuming string can be sorted
    string = sorted(list(string))
   
    for i in range(1, len(string)):
        # Check if next index is valid
        if string[i-1] == string[i]:
            return False
    return True

        
    
    
if __name__ == '__main__':
    print(isUnique_nods('hello'))
    print(isUnique_nods('asiod'))