class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            return 0
        
        maxP = 0
        bd = prices[0]
        sd = prices[1]
        for i in range(len(prices)-1):
            if bd > sd:
                bd = sd
                
            sd = prices[i+1]
            profit = sd-bd
            maxP = max(maxP, profit)
        
        return maxP
            
            