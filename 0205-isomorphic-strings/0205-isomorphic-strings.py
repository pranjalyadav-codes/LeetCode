class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping = {}
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if char_s in mapping:
                if mapping[char_s] != char_t:
                    return False
            else:
                if char_t in mapping.values():
                    return False
                mapping[char_s] = char_t
        return True