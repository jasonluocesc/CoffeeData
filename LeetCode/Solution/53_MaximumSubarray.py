class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #max subarray() 0+a[i]
        if not nums:
            return 0
        currentSum = maxSum = nums[0]
        for num in nums[1:]:
            currentSum = max(num,currentSum+num)
            maxSum = max(currentSum,maxSum)
        return maxSum

print(Solution().maxSubArray([-1,2,-3,4,5,6]))

