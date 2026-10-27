class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = 0
        running = 0
        seen = {0: 1}                
        for x in nums:
            running += x
            r = running % k           
            count += seen.get(r, 0)   
            seen[r] = seen.get(r, 0) + 1
        return count