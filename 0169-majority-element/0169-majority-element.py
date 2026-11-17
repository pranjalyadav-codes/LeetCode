class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        
        maximum  = 0
        result = 0
        for key, value in freq.items():
            if value > maximum:
                maximum = value
                result = key 

        return result