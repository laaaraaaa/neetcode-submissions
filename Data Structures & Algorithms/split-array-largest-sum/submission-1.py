class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        def maxsplit(largest):
            subarray = 1
            currsum = 0
            for n in nums:
                currsum += n
                if currsum > largest:
                    subarray += 1
                    if subarray > k:
                        return False
                    currsum = n
            return True
        


        while l <= r:
            m = (l+r) // 2
            if maxsplit(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
        