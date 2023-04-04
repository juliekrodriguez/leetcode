def majorityElement(nums):
    # Create a dictionary to store the frequency of each element
    freq_dict = {}
    
    # Iterate through the array and update the dictionary
    for num in nums:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # Find the element with frequency greater than ⌊n / 2⌋
    for key, value in freq_dict.items():
        if value > len(nums) // 2:
            return key

print(majorityElement([3, 2, 3]))   # Output: 3
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))   # Output: 2


#o(n) time
#o(n) space
