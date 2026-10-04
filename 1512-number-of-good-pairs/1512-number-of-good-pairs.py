class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        result = 0

        for num in nums:
            if num in count:
                result += count[num]

            count[num] = count.get(num, 0) + 1

        return result