class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr = 0
        best = float("inf")
        for r in range(len(nums)):
            curr += nums[r]
            while curr >= target:
                best = min(best, r - l + 1)
                curr -= nums[l] 
                l += 1

        return best if best != float("inf") else 0