class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        theOtherDict={}
        for index,item in enumerate(nums):
            if item in theOtherDict:
                return [theOtherDict[item], index]
            else:
                theOtherDict[target-item] = index


def execute():
    nums = [3, 2, 4]
    target = 6
    sol = Solution()
    print(sol.twoSum(nums=nums, target=target))


if __name__=="__main__":
    execute()