# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 15:07:39 2019
Leetcode: Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true

Note:

    You may assume that all inputs are consist of lowercase letters a-z.
    All inputs are guaranteed to be non-empty strings.


Time Complexity: O(n), for inserting and searching for word dependent on length of word
Space Complexity: O(n), stores words by their prefixes  

@author: bohan

"""



class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        
        t['#'] = '#'
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self.trie
        for w in word:
            if w not in t:
                return False
            t = t[w]
        
        if '#' in t:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.trie
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)