class Solution:

    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        # Your code here
        ar = []
        maxi = max(arr)
        if maxi < 0:
            return 1
        posarr = list(filter(lambda n: n > 0, arr))
        upa = list(set(posarr))
        if len(upa) == 0:
            return 1
        if len(upa) == max(upa):
            return max(upa) + 1
        else:
            for i in range(1, max(upa)):
                if i not in upa:
                    return i
                    break