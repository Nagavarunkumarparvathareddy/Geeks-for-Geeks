class Solution:
	def matSearch(self, mat, x):
        nums = []
        for ele in mat:
            for e in ele:
                nums.append(e)
        if x in nums:
            return True
        else:
            return False
