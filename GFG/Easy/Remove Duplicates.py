class Solution:
    def removeDups(self, str):
        # code here
        ans = []
        res = ''
        for ele in list(str):
            if ele not in ans:
                ans.append(ele)
        for ele in ans:
            res += ele
        return res

