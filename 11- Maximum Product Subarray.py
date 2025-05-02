#User function Template for python3
class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self,arr):
        # code here
        n = len(arr)
        maxProd = float('-inf')
        
        #left to right to store product from left to right
        leftToRight = 1
        #right to left to store product from right to left
        rightToLeft = 1
        
        for i in range(n):
            if leftToRight == 0:
                leftToRight = 1
            if rightToLeft == 0:
                rightToLeft = 1
            #calculate product from index left to right
            leftToRight *= arr[i]
            #calculate product from index right to left
            j = n - i - 1
            rightToLeft *= arr[j]
            maxProd = max(leftToRight,rightToLeft,maxProd)
        return maxProd