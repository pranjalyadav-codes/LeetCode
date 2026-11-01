class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        ans = 0
        while start <= end:
            mid = (start + end)//2
            midSquare = mid * mid

            if midSquare > x:
                end = mid - 1
            else:
                ans = mid 
                start = mid + 1

        return ans