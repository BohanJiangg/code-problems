# -*- coding: utf-8 -*-
"""
Created on June 12 2019
Leetcode: Replace Words

In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Note:
The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000

Time Complexity O(n*m*k), where n is the number of words in the dict, m is the difference between maxRoot length and minRoot length, and k is the length of the dict. 
Space Complexity: O(N), Need another string to store output sentence. 
@author: bohan
"""

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        minRoot = len(min(dict, key=len))
        maxRoot = len(max(dict, key=len))
        
        outputSentence = ''
        for word in sentence.split(' '):
            tempWord = word
            for i in range(minRoot, maxRoot+1):
                if i <= len(tempWord): 
                    
                    if tempWord[0:i] in dict:
                        tempWord = tempWord[0:i]
                        break
            
            if outputSentence == '':
                outputSentence = tempWord
            else:
                outputSentence = outputSentence + ' ' + tempWord
        
        return outputSentence

