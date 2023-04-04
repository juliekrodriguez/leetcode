'''
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


use a set to see did i see this before in nums

key points: set and length comparision

'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
       # place array nums in set
        mySet = set(nums)
        # compare length of new set with length of nums array
        return len(mySet) != len(nums)

