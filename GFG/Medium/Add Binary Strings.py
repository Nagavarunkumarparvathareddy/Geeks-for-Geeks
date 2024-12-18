class Solution:
	def addBinary(self, s1, s2):
		# code here
		s1 = int(s1,2)
		s2 = int(s2,2)
		s3 = s1+s2
		ans = str(bin(s3))
		return ans[2:]