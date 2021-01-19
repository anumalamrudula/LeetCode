class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max1 = 0
        count = 0
        index = -1
        for i in range(len(nums)):
            if nums[i]==1:
                count += 1
            else:
                count = i - index
                index = i
            max1 = max(count,max1)
        return max1