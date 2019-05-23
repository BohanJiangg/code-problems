# -*- coding: utf-8 -*-
"""
Created on Sun May 12 13:40:57 2019

CTCI: Problem 1.6 - String Compression
Time Complexity: O(n), iterate through s only once
Space Complexity: O(n), in general, since in worst case where no characters match the string is twice as long 

@author: bohan
"""


def string_compression(s):
    
    prev_char = ''
    compressed_string = ''
    charCount = 0
    for char in s:
        if prev_char:
            if char == prev_char:
                charCount += 1
            else:
                compressed_string = compressed_string + prev_char + str(charCount)
                prev_char = char
                charCount = 1
        else:
            prev_char = char
            charCount = 1
    
    compressed_string = compressed_string + prev_char + str(charCount)
    
    
    if len(compressed_string) > len(s):
        return s
    else:
        return compressed_string
    


if __name__ == "__main__":
    print(string_compression('aabccccaaa'))
    print(string_compression('abcd'))
    
    