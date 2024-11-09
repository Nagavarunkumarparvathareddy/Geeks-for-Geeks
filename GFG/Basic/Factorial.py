class Solution:
    def factorial (self, N):
        # code here
        ans = 1
        for i in range(1,N+1):
            ans = ans*i
        return ans