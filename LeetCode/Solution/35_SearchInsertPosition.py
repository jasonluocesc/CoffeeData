class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=0
        for num in nums:
            if num<target:
                i+=1
            else:
                return i
        return len(nums)



print(Solution().searchInsert([3,5,6,7],5))