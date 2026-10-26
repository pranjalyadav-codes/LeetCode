class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atMost(k):
            freq = {}
            left = 0
            count = 0
            for right, num in enumerate(nums):
                freq[num] = freq.get(num, 0) + 1

                while len(freq) > k:
                    left_num = nums[left]
                    freq[left_num] -= 1

                    if freq[left_num] == 0:
                        del freq[left_num]

                    left += 1

                count += right - left + 1
            return count

        return atMost(k) - atMost(k-1)