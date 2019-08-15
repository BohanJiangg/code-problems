# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 11:36:07 2019

Leetcode: Accounts Merge

Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:

Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.


Time Complexity: O(sum(len(accounts))*log(len(accounts))), to build the graph and then sort 
Space Complexity: O(sum(len(accounts))), need to build the graph and search

@author: bohan
"""


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        
        if not accounts:
            return None

        if len(accounts) == 1:
            return accounts 

        # graph of email addresses to a list of other email addresses
        # {"johnsmith@mail.com": set('john_newyork@mail.com', 'johnnybravo@mail.com')}
        graph = collections.defaultdict(set)
        # dict of person's one email to name
        # to run DFS on
        email_to_name = {}

        for item in accounts:
            name = item[0]
        
            for email in item[1:]:
                graph[email].add(item[1])
                graph[item[1]].add(email)
                email_to_name[email] = name
        
        
        
        visited = set()
        toRet = []

        for email in graph:
            if email not in visited:
                visited.add(email)
                stack = [email]
                emails = []
                while stack:
                    curr = stack.pop(0)
                    emails.append(curr)
                    for nei in graph[curr]:
                        if nei not in visited:
                            stack.append(nei)
                            visited.add(nei)
                
                toRet.append([email_to_name[email]] + sorted(emails))
        
        return toRet



