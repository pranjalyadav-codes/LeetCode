class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start = 0
        max_len = 0

        for i in range(n):
            # Case 1: Odd-length palindrome
            left = right = i

            while left >= 0 and right < n and s[left] == s[right]:
                length = right - left + 1

                if length > max_len:
                    start = left
                    max_len = length

                left -= 1
                right += 1

            # Case 2: Even-length palindrome
            left, right = i, i + 1

            while left >= 0 and right < n and s[left] == s[right]:
                length = right - left + 1

                if length > max_len:
                    start = left
                    max_len = length

                left -= 1
                right += 1

        return s[start:start + max_len]