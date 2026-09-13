class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for n in numset:
            if not (n-1) in numset:
                length = 0
                while (n + length) in numset:
                    length += 1
                longest = max(longest, length)
        return longest
        