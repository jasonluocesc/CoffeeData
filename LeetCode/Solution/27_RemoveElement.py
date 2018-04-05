class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        d = 0
        for i in range(0,len(nums)):
            if nums[i] != val:
                nums[d] = nums[i]
                d+=1
        return d

print(Solution().removeElement([3,2,2,3,2],3))