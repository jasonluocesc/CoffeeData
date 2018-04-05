class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0 or len(nums)==1:
            return len(nums)
        id = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[id] = nums[i]
                id = id + 1
        return id
print(Solution().removeDuplicates([-6,-6,2,3,4]))