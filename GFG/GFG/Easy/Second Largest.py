arr = list(set(arr))
arr = sorted(arr)
l = len(arr)
if len(arr) < 2:
    return -1
if len(arr) >=2 and arr[-1] == arr[-2]:
    return -1
else:
    return arr[-2]