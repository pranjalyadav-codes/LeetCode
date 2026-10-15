class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first = second = third = float('-inf')

        for num in nums:
            if num == first or num == second or num == third:
                continue

            if num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num

        return first if third == float('-inf') else third