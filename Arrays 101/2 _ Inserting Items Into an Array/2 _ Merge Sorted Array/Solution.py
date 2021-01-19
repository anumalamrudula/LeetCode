class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        i=0
        j=0
        k=0
        if n==0:
            pass
        else:
            for k in range(m+n):
                if j==n or (nums1[i] <= nums2[j] and i<m):
                    temp.append(nums1[i])
                    i = i+1
                else:                
                    temp.append(nums2[j])
                    j = j+1
            for i in range(len(temp)):
                nums1[i] = temp[i]