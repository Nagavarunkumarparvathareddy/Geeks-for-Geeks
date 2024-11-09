class Solution:
    def Maximize(self, arr): 
        # Complete the function
        s = sorted(arr)
        prod = 0
        for i in range(len(s)):
            prod += s[i]*i
        result = prod % (10**9+7)
        return result