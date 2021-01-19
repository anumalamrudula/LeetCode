class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        temp = []  
        for n in arr:
            if n==0:
                temp.append(n)
            temp.append(n)
        arr1 = temp[:len(arr)]
        
        for i in range(len(arr)):
            arr[i] = arr1[i]