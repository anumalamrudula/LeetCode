class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        maxN = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2,-1,-1):
            temp = max(maxN,arr[i])
            arr[i] = maxN
            maxN = temp
        return arr