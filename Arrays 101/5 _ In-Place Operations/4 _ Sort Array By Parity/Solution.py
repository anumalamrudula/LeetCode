class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        #return [e for e in A if e%2==0] + [o for o in A if o%2!=0]

        i=0
        for j in range(len(A)):
            if A[j]%2==0:
                temp = A[j]
                A[j] = A[i]
                A[i] = temp
                i=i+1
        return A    