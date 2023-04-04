'''
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

inital: make a hashmap, does value = 2? then put in res array and return. - wrong idea here

correct sol: make a bucket sort where i is len of array and then place new array(most element)
to match with the index.
'''
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # create an empty dictionary to store the frequency of each number
        freq = {}
        # create an empty list to store the most frequent numbers
        res = []
        # iterate through each number in the input list
        for num in nums:
            # increment the frequency of the current number in the dictionary
            freq[num] = freq.get(num, 0) + 1
            # if the frequency of the current number is equal to k,
            # append the current number to the result list
            if freq[num] == k:
                res.append(num)
        # return the list of the most frequent numbers
        return res

# create an instance of the Solution class
s = Solution()
# call the topKFrequent method with nums=[1, 2] and k=2
result = s.topKFrequent(nums=[1, 2], k=2)
# print the result (should be [1, 2])
print(result)
