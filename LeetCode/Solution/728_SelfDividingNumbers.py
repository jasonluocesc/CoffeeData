
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for num in range(left,right+1):
            if isSelfDividing(num):
                result.append(num)

        return result

def isSelfDividing(x):
    for digit in str(x):
        if digit=="0" or x%int(digit)!=0:
            return False
    return True

print(Solution().selfDividingNumbers(1,22))