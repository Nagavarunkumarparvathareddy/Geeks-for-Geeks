##Your code here
        cursum = 0
        maxsum = float('-inf')
        for i in range(0,len(arr)):
            cursum = max(arr[i],(cursum+arr[i]))
            maxsum = max(maxsum,cursum)
        return maxsum