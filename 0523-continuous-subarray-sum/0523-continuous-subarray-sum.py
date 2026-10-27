class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        
        prefix_sum = 0
        freq = {0: -1}
        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k

            if remainder in freq:
                if i - freq[remainder] >= 2:
                    return True
            else:
                freq[remainder] = i

        return False