class Solution:
    def find(self, arr, x):
        ans = []
        # code here
        if x not in arr:
            return [-1, -1]
        else:
            for i in range(len(arr)):
                if arr[i] == x:
                    ans.append(i)
            return [ans[0], ans[-1]]
