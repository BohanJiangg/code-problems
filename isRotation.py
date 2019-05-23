# -*- coding: utf-8 -*-
"""
Created on Tue May 21 20:21:50 2019

CTCI: Problem 1.9 - String Rotation
Time Complexity: O(n), one loop the length of s1 in the worst case
Space Complexity: O(n), need to keep s2 in a placeholder while rotation

@author: bohan
"""




def isRotation (s1, s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        s2 = s2[-1]+s2[0:-1]
        if(s2 == s1):
            return True
    
    
    return False


def isRotation2(s1,s2):
    if len(s1) != len(s2) or len(s1) == 0 or len(s2) == 0:
        return False
    
    # This goes off the reasoning that if s1 is a rotation of s2, then there is a cuttoff point
    # First part is x, second part is y, and xy=s1 and yx=s2.
    # but this means that yx always in xyxy, so check if s2 in s1+s1
    if s2 in s1+s1:
        return True
    
    return False

if __name__ == '__main__':
    print(isRotation('waterbottle', 'erbottlewat'))
    print(isRotation('waterbottle', 'bottlweater'))
    
    print(isRotation2('waterbottle', 'erbottlewat'))
    print(isRotation2('waterbottle', 'bottlweater'))
