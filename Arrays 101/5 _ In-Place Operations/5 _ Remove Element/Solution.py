class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """        
        # c = 0
        # temp = []
        # for i in range(len(nums)):
        #     if nums[i] == val:
        #         c = c + 1
        #     else:
        #         temp.append(nums[i])
        # for j in range(len(nums)):
        #     if j < len(temp):
        #         nums[j] = temp[j]
        #     else:
        #         nums[j] = 0
        # return len(temp)
                
        i=0
        for n in nums:
            if n!=val:
                nums[i] = n
                i = i+1
        return i