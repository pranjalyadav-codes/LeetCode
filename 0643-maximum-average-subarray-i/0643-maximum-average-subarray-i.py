class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)

        window_sum = sum(nums[:k])
        max_sum = window_sum

        for j in range(k, n):
            window_sum += nums[j] - nums[j - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k
