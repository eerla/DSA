class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        maxP, minP = 1, 1
        
        for n in nums:
            temp = maxP
            maxP = max(n*maxP, n*minP, n)
            minP = min(n*temp, n*minP, n)
            
            res = max(res, maxP, minP)
        
        return res
            