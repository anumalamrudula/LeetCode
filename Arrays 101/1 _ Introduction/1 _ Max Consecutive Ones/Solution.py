class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 1 not in nums:
            return 0
        c=0
        temp=0
        for i in range(0,len(nums)):
            if nums[i]==1:
                temp = temp+1
                c = max(c,temp)
            else:
                 temp = 0
        return c
        
        #return len(max("".join(map(str, nums)).split("0")))