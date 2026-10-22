
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()  # Stores indices
        result = []

        for right in range(len(nums)):

            # 1. Remove indices outside the current window
            while dq and dq[0] <= right - k:
                dq.popleft()

            # 2. Remove smaller or equal values from the back
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            # 3. Add the current index
            dq.append(right)

            # 4. Record maximum once the first window is complete
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result
