class Solution:
    def reverseArray(self, arr):
        # code here
        newarr = arr.copy()
        l = len(arr)
        j = 0
        for i in range(l-1,-1,-1):
            arr[i] = newarr[j]
            j += 1
        return arr