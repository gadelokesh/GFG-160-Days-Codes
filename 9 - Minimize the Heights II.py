class Solution:
    def getMinDiff(self, arr,k):
        # code here
        n = len(arr)
        arr.sort()
        
        #if we increase al heights by k or decrease all heights by k,th
        #the result will be arr[n-1]-arr[0]
        
        res = arr[n-1]-arr[0]
        
        #for all indices i ,increment arr[0....i-1]by k and 
        #decrement arr[i .....n-1] by k
        
        for i in range(1,len(arr)):
            #imposible to decrement height of ith tower by k
            #continue to the next tower
            if arr[i] - k < 0:
                continue
            
            #minimum height after modification
            minH = min(arr[0]+k,arr[i]-k)
            
            #maximum height after modification
            maxH = max(arr[i-1]+k,arr[n-1]-k)
            
            #store the min diffrences as result
            res = min(res,maxH - minH)
        return res