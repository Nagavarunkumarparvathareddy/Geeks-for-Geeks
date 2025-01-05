class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        l = len(arr)
        if d <= len(arr):
            arr1 = arr[d:]
            arr2 = arr[0:d]
            result = arr1+arr2
            for i in range(len(arr)):
                arr[i] = result[i]
            return arr
                
        else:
            a = d%l
            if a == d:
                return arr
            else:
                arr1 = arr[a:]
                arr2 = arr[0:a]
                arr3 = arr1+arr2
                for i in range(len(arr)):
                    arr[i] = arr3[i]
                return arr