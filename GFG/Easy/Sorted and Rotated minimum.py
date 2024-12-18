class Solution:
    def findMin(self, arr):
        #complete the function here
        s = list(set(arr))
        minimum = s[0]
        for i in range(len(s)):
            if s[i] < minimum:
                minimum = s[i]
        return minimum