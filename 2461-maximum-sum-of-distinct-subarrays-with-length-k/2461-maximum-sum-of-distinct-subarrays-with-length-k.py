class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n < k:
            return 0
        freq = {}
        window_sum = 0
        max_sum = 0

        for right in range(n):
            # Add the new element
            x = nums[right]
            window_sum += x
            freq[x] = freq.get(x, 0) + 1

            # Keep window size at most k
            if right >= k:
                left_element = nums[right - k]
                window_sum -= left_element
                freq[left_element] -= 1

                if freq[left_element] == 0:
                    del freq[left_element]

            # Check window size and distinctness
            if right >= k - 1 and len(freq) == k:
                max_sum = max(max_sum, window_sum)

        return max_sum