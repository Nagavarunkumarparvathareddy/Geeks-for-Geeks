class Solution:
    def search(self,arr,key):
        # Complete this function
        if key not in arr:
            return -1
        else:
            for i in range(len(arr)):
                if arr[i] == key:
                    return i