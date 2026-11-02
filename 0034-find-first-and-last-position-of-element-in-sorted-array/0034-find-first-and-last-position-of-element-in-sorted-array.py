class Solution:
    def lower_bound(self, nums, target):
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high)//2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low

    def upper_bound(self, nums, target):
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high)//2
            if nums[mid] <= target:
                low = mid +1
            else:
                high = mid 

        return low 

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lower_bound(nums, target)
        ub = self.upper_bound(nums, target)
        
        if lb == ub :
            return [-1, -1]
        else:
            return [lb, ub - 1]