class Solution:
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        c =a+b
        c = set(c)
        c = sorted(c)
        return c