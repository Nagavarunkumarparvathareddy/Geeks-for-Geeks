
class Solution:

    def kthSmallest(self, arr ,k):
        s = sorted(list(arr))
        return s[ k -1]



