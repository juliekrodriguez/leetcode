'''
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
'''
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        #make hashset
        hashset = set()
        # for everything in the array
        for n in nums:
            # if its already in the array
            if n in hashset:
                return True
            hashset.add(n)
        # else there is only distinct
        return False

