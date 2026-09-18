class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}

        for letter in s:
            hashmap[letter] = 1 + hashmap.get(letter, 0)
        
        for i, letter in enumerate(s):
            if hashmap[letter] == 1:
                return i
        
        return -1
        