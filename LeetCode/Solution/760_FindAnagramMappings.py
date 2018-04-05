class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        result = [0]*len(A)
        for i in range(0,len(A)):
            for j in range(0,len(B)):
                if B[j]==A[i]:
                    result[i]=j
        return result

print(Solution().anagramMappings([12,28,46,32,50],[50,12,32,46,28]))