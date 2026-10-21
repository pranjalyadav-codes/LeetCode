class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        freq = {}
        window_sum = 0
        max_sum = 0
        left = 0
        for right in range(len(nums)):
            num = nums[right]
            window_sum += num
            freq[num] = freq.get(num, 0) + 1

            if right - left + 1 > k:
                left_num = nums[left]
                window_sum -= left_num
                freq[left_num] -= 1

                if freq[left_num] == 0:
                    del freq[left_num]
                left += 1
            if right - left + 1 == k and len(freq) == k:
                max_sum = max(max_sum, window_sum)

        return max_sum