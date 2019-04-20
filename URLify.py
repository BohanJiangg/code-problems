# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 09:28:54 2019

CTCI: Problem 1.3 - URLify
Time Complexity: O(n), loop through string to repalce all spaces with %20
Space Complexity: O(n), copy operation when converting string to list and slicing string

@author: bohan
"""



'''
Function that replaces all space characters in string in place with '%20'
trueLength is just the length of all the spaces and characters in the string
'''
def URLify(string, trueLength):
    string = list(string[0:trueLength])

    for i in range(trueLength):
        if string[i] == ' ':
            string[i] = '%20'
    
    return ''.join(string)
        

    
    
    

    
if __name__ == '__main__':
    print(URLify('Mr John Smith      ', 13))
    print(URLify('Hello lol  ', 9))