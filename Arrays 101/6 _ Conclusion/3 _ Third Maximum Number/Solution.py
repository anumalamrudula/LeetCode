class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxs = set()
        for n in nums:
            maxs.add(n)
            if len(maxs)>3:
                maxs.remove(min(maxs))
        if len(maxs)<3:
            return max(maxs)
        else:
            return min(maxs)