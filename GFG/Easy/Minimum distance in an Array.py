class Solution:
    def minDist(self, arr, n, x, y):
        a_arr = []
        b_arr = []
        mindiff = float('inf')
        if x not in arr or y not in arr:
            return -1
        else:
            for i in range(len(arr)):
                if arr[i] == x:
                    a = i
                    a_arr.append(a)
                if arr[i] == y:
                    b = i
                    b_arr.append(b)
            for a in a_arr:
                for b in b_arr:
                    diff = abs(a-b)
                    if diff < mindiff:
                        mindiff = diff
            return mindiff
                    
                    
