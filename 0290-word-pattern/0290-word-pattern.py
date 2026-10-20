class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
    
        # Length check - "aab" vs "cat dog" → False
        if len(pattern) != len(words):
            return False
    
        char_to_word = {}  # 'a' -> 'dog'
        word_to_char = {}  # 'dog' -> 'a'
    
        for ch, word in zip(pattern, words):
            if ch in char_to_word:
                if char_to_word[ch] != word:
                    return False
            else:
                # New char, but word already mapped to another char?
                if word in word_to_char:
                    return False
                char_to_word[ch] = word
                word_to_char[word] = ch
    
        return True
