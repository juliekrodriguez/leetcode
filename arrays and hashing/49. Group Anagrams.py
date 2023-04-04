'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

inital: take the strings within the array and sort them
'''
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        h = {}  # create an empty dictionary to store the sorted word as key and its anagrams as value
        for word in strs:  # iterate through the input list of strings
            sortedWord = ''.join(sorted(word))  # sort the characters of the current word and join them to form a new string
            if sortedWord not in h:  # if the new string is not already in the dictionary,
                h[sortedWord] = [word]  # add the new string as a key and the current word as the first value in the list
            else:  # if the new string is already in the dictionary,
                h[sortedWord].append(word)  # append the current word to the list of values for that key
        final = []  # create an empty list to store the final result
        for value in h.values():  # iterate through the values in the dictionary
            final.append(value)  # append each list of anagrams to the final list
        return final  # return the final list of lists of anagrams

# Call the groupAnagrams function with an example input

s = Solution()  # create an instance of the Solution class
result = s.groupAnagrams(strs=["eat","tea","tan","ate","nat","bat"])  # call the groupAnagrams method on the instance and store the result
print(result)  # print the result


        

