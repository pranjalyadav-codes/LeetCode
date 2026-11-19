class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 0:
            median = (nums[len(nums)//2 - 1] + nums[len(nums)//2])/2
        else:
            median = nums[len(nums)//2]
        return median