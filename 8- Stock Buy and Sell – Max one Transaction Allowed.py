class Solution:
    def maximumProfit(self, prices):
        # code here
        minSoFar = prices[0]
        res = 0
        
        # update the min value seen so far if we see smaller
    
        for i in range(1,len(prices)):
            minSoFar = min(minSoFar,prices[i])
        
        #update the result if we got more profit
            
            res = max(res,prices[i] - minSoFar)
            
        return res