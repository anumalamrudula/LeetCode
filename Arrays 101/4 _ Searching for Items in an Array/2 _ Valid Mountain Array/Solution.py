class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)
        i=0
        j=n-1
        if len(arr) >= 3:
            while(i+1<n and arr[i]<arr[i+1]):
                i = i+1
            while(j>0 and arr[j-1]>arr[j]):
                j = j-1
            if(i>0 and i==j and j<n-1):
                return True
            else:
                return False
        else:
            return False