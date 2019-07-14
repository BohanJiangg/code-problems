# -*- coding: utf-8 -*-
"""
Created on Sun May 12 13:40:57 2019

Leetcode: String Compression
CTCI: Problem 1.6 - String Compression

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Time Complexity: O(n), iterate through s only once
Space Complexity: O(n), in general, since in worst case where no characters match the string is twice as long 

@author: bohan
"""


def string_compression(chars):
    
    prev_char = ''
    charCount = 0
    
    for i in range(len(chars)):
        char = chars.pop(0)
        if prev_char:
            if char == prev_char:
                charCount += 1
            else:
                if charCount > 1:
                    chars.append(str(prev_char))
                    for ch in str(charCount):
                        chars.append(ch)
                else:
                    chars.append(str(prev_char))
                prev_char = char
                charCount = 1
        else:
            prev_char = char
            charCount = 1
    
    chars.append(str(prev_char))
    
    if charCount > 1:
        for ch in str(charCount):
            chars.append(ch)
    
    
    return len(chars)
    


if __name__ == "__main__":
    print(string_compression('aabccccaaa'))
    print(string_compression('abcd'))
    
    