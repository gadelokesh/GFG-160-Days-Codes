class Solution:
    def nextPermutation(self, arr):
        # code here
        n = len(arr)
    # find the pivot index 
        pivot = -1
        for i in range(n-2,-1,-1):
            if arr[i] < arr[i+1]:
                pivot = i 
                break
    
    # if pivot point doesn't exist
    #reverse the whole array
        if pivot == -1:
            arr.reverse()
            return
    
    #find the element from the right that is greater than pivot
        
        for i in range(n-1,pivot,-1):
            if arr[i] > arr[pivot]:
                arr[i],arr[pivot] = arr[pivot],arr[i]
                break
            
    #Reverse the elements from pivot+1 to end in place 
        left,right = pivot+1,n-1
        while left < right:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1