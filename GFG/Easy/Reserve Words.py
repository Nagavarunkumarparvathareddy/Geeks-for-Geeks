def reverseWords(self,str):
        # code here 
        s = str.split('.')
        l = len(s)
        dot = '.'
        ans = ''
        i = l-1
        while(i >= 0):
            ans += s[i]
            i -= 1
            if i >= 0:
                ans += dot
        return ans