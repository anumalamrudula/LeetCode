class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(0,len(nums)):
            if nums[j]!=0:
                nums[i] = nums[j]
                i=i+1
        for k in range(i,len(nums)):
            nums[k]=0
        return nums