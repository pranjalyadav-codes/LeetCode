class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}
        for char in magazine:
            freq[char] = freq.get(char, 0) + 1
        for char in ransomNote:
            if freq.get(char, 0) == 0:
                return False

            freq[char] -= 1

        return True