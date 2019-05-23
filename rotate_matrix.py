# -*- coding: utf-8 -*-
"""
Created on Sun May 12 14:08:22 2019

CTCI: Problem 1.7 - Rotate Matrix
Time Complexity: O(n),
Space Complexity: O(n),  

@author: bohan
"""



# function that rotates the matrix by 90 degrees
def rotate_matrix(coords_list):
    
    
    
    
    
    
    return coords_list





if __name__ == "__main__":
    # Size of image
    m = 3
    n = 3
    
    image_coords = []
    num = 0
    for i in range(1,m+1):
        row = []
        for j in range(1,n+1):
            num+=1
            row.append(num)
        image_coords.append(row)
            
    print(image_coords)
    print(rotate_matrix(image_coords))