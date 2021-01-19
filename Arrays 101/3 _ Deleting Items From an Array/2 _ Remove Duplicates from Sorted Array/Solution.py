class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        i = 1
        for j in range(1,len(nums)):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i=i+1
        return i