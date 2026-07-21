class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count = 0
        res = float("inf")
        l = 0
        for r in range(len(nums)):
            count += nums[r]
            while count >= target:
                res = min(res, r-l+1)
                count -= nums[l]
                l += 1
        
        return 0 if res == float("inf") else res

        