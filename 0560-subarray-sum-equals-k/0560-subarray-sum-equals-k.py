class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        prefix = 0
        count = 0
        for num in nums:
            prefix += num
            count += freq.get(prefix - k, 0)
            freq[prefix] = freq.get(prefix, 0) + 1
        return count 