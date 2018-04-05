class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x>=0:
            temp1 = str(x)
            temp2 = temp1
            if temp1[::-1] == temp2:
                return True
            else:
                return False
        else:

            return False

def execute():
    num = -2147447412
    sol = Solution()
    print(sol.isPalindrome(num))


if __name__=="__main__":
    execute()