class Solution:
    def evenlyDivides (self, N):
        # code here
        s = str(N)
        sl = list(s)
        ss = list(sl)
        set_lst = [int(x) for x in ss]
        count = 0
        for ele in set_lst:
            if ele == 0:
                count += 0
            elif N % ele == 0:
                count += 1
        return count

