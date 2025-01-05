class Solution:

    # Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x):
        # code here
        nums = []
        for ele in mat:
            for e in ele:
                nums.append(e)
        if x in nums:
            return True
        else:
            return False