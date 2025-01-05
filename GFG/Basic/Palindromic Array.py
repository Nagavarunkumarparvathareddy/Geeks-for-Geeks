def PalinArray(arr):
    # Code here
    for ele in arr:
        if str(ele) != str(ele)[::-1]:
            return False
    return True
