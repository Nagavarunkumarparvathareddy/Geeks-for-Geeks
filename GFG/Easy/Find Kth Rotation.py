class Solution:
    def findKRotation(self, arr):
        # code here
        sorted_arr = sorted(arr)
        if arr == sorted_arr:
            return 0
        for i in range(len(arr)):
            if arr[i] == sorted_arr[0]:
                return i