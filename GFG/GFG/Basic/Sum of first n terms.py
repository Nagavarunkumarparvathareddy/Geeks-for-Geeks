class Solution:
    def sumOfSeries(self,n):
        #code here
        ans=[i**3 for i in range(1,n+1)]
        return sum(ans)
