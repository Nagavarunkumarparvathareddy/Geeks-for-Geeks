        #Code Here
        arr1 = set(arr1)
        arr2 = set(arr2)
        arr3 = set(arr3)
        res = arr1.intersection(arr2)
        res = res.intersection(arr3)
        res = list(sorted(res))
        return res