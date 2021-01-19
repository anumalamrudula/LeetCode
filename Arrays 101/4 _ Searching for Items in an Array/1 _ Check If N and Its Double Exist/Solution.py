class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        s = set()
        for n in arr:
            if n*2 in s:
                return True
            if n/2 in s and n%2==0:
                return True            
            s.add(n)
        return False