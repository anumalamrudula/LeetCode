class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        return len([n for n in nums if len(str(n))%2 == 0])