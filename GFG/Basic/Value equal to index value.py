def valueEqualToIndex(self, arr):
        new = []
        l = len(arr)
        for i in range(l):
            if arr[i] == i+1:
                new.append(arr[i])
        return new