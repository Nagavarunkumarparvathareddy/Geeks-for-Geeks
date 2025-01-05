class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        unique =list(set(arr))
        l =len(arr)
        target = l/3
        newarr = []
        for ele in unique:
            if arr.count(ele) > target:
                newarr.append(ele)
        ans = sorted(newarr)
        return ans
        
