class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        elif n==2:
            return "2"

        else:
            return Solution().countAndSay(n-1)