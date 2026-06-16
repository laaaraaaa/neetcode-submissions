class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_words = []
        l = 0
        r = 0
        while l < len(word1) or r < len(word2):
            if l < len(word1):
                merged_words.append(str(word1[l]))
                l += 1
            if r < len(word2):
                merged_words.append(str(word2[r]))
                r += 1
        return "".join(merged_words)
        