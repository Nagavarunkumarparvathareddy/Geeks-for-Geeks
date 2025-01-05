class Solution:

    # Function to check if Kth bit is set or not.
    def checkKthBit(self, n, k):
        # Your code here
        binary = str(bin(n))
        b = binary[2:]
        a = b[::-1]
        if k >= len(a):
            return False
        else:
            if a[k] == '1':
                return True
            else:
                return False