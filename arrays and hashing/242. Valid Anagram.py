'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

inital: use dict to view how many times did this letter show up in t
make another dict to view how many times did this letter show up in s
compare s and t dictonary's
TC: O(S+T)
SC: O(S+T)

make one dict to put s in, then compare this dict with t. 
TC: O(S+T)
SC: O(T)

look at s string and then sort s, now look at t string and sort t, now
make pointer at s and keep comparing with s and t. 
TC: O(NLOGN)
SC: O(N)

'''
class Solution:
    # this solution just compares sorted word S, with sorted word T.
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    # this solution has 2 dictonarys



    def isAnagram1(self, s: str, t: str) -> bool:
        # first check, are the lenghts even the same
        if len(s) != len(t):
            return False
        # init both dictonary
        countS, countT = {}, {}
        # it through length s, since they both same len 
        for i in range(len(s)): # get around key error w 'get' func
            countS[s[i]] = 1+ countS.get(s[i], 0) # counting occur of each char in string s
            countT[t[i]] = 1+ countT.get(t[i], 0) # same w t
        # it thru hashmaps, make sure counts are the saem
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True

