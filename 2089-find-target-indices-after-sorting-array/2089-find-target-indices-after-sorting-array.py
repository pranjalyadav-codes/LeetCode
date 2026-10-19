class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        smaller = sum(x < target for x in nums)
        equal = sum(x == target for x in nums)

        return list(range(smaller, smaller + equal))