class Solution:
    def transitionPoint(self,arr): 
        # Code here
        for i in range(len(arr)):
            if arr[i] == 1:
                return i
        else:
            return -1