class Solution:
    def intersectionWithDuplicates(self, a, b):
        # code here
        s1 = set(a)
        s2 = set(b)
        ans = s1.intersection(s2)
        return list(ans)
