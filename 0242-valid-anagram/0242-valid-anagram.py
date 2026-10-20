class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = [0] * 26
        for i in range(len(s)):
            freq[ord(s[i]) - ord("a")] += 1
            freq[ord(t[i]) - ord("a")] -= 1

        return all(count == 0 for count in freq)