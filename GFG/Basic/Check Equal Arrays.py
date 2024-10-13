        #code here
        arr1 = sorted(arr1)
        arr2 = sorted(arr2)
        l1 = len(arr1)
        l2 = len(arr2)
        if l1==l2:
            if arr1 == arr2:
                return 'true'
        else:
            return 'false'