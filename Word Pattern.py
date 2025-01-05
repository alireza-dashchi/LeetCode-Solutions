class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(" ")  # List of words from the string
        if len(pattern) != len(words):  # Ensure pattern length matches number of words
            return False
        
        char_to_word = {}  # Dictionary to map pattern characters to words
        for char, word in zip(pattern, words):
            if char not in char_to_word:
                if word in char_to_word.values():  # Ensure no duplicate word mapping
                    return False
                char_to_word[char] = word
            elif char_to_word[char] != word:  # Ensure consistent mapping
                return False
        
        return True