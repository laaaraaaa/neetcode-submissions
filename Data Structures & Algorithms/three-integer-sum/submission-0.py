class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                ThreeSum = n + nums[l] + nums[r]
                if ThreeSum > 0:
                    r = r - 1
                elif ThreeSum < 0:
                    l = l + 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l = l + 1 
                    while nums[l] == nums[l-1] and l < r:
                        l = l + 1
        return res
        