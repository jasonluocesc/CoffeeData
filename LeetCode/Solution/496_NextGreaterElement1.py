class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = [0]*len(nums1)
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                if j<len(nums2)-1:
                    if nums1[i]==nums2[j] and nums1[i]<nums2[j+1]:
                        result[i]=nums2[j+1]
                    elif nums1[i]==nums2[j]:
                        result[i]=-1
                else:
                    if nums1[i]==nums2[j]:
                        result[i]=-1

        return result
print(Solution().nextGreaterElement([2,4],[1,2,3,4]))