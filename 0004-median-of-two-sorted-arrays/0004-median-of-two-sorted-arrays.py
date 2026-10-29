class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        l = len(nums)
        if l % 2 == 0:
            median = (nums[l//2 - 1] + nums[(l//2)])/2
        else:
            median = nums[l//2]
        return median