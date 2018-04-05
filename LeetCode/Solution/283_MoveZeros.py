class Solution:
    def moveZeroes(self, nums):
     for num in nums:
         if num == 0:
             nums.remove(num)
             nums.append(0)
     return nums


a = [0,1,0,12,6,0]
x = Solution()
y = x.moveZeroes(a)
print(y)


