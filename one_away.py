# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 10:15:01 2019

CTCI: Problem 1.5 - One Away
Time Complexity: O(n), where n is the string with the one character longer, one-time pass through
Space Complexity: O(1), only need boolean flags and a few variable pointers

@author: bohan
"""

'''
Function that determines if two strings are one edit away (or 0)
Edit is defined as inserting, removing, or replacing a character
'''
def oneAway(str1, str2):
    
    # Flag indicating first difference found
    firstDiff = False
    
    # if same length, then must be replace
    if (len(str1) == len(str2)):
        
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if firstDiff:
                    return False
                else:
                    firstDiff = True
        return True
    
    elif abs(len(str1) - len(str2)) == 1:
        
        if len(str1) > len(str2):
            longstr = str1
            shortstr = str2
        else:
            longstr = str2
            shortstr = str1
         
        
        shortIndex = 0
        for longIndex in range(len(shortstr)):
            if shortstr[shortIndex] != longstr[longIndex]:
                if firstDiff:
                    return False
                else:
                    firstDiff = True
                    shortIndex -=1
            
            shortIndex+=1
        
        return True   
            


if __name__ == '__main__':
    print(oneAway('pale','ple')) #true
    print(oneAway('pales','pale')) #true
    print(oneAway('pale','bale')) #true
    print(oneAway('pale','bake')) #false