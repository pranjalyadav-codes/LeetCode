class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        freq = {}
        res = []
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        for i in freq.keys():
            if freq[i] > n/3:
                res.append(i)
        return res