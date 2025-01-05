class Solution:

    def kthElement(self, a, b, k):
        arr = []
        arr = a+b
        array = sorted(arr)
        return array[k-1]