class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        res = 0
        
    #keep on adding the diffrence between adjacent when the prices a
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res
