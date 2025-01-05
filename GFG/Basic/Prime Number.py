
#User function Template for python3
import math
class Solution:
    def isPrime (self, N):
        # code here
        if N <= 1:
            return 0
        else:
            for i in range(2,int(math.sqrt(N))+1):
                if N % i == 0:
                    return 0
            return 1

