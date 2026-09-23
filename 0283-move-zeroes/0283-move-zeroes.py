class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
            # Swap the non-zero element to the write position
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
        