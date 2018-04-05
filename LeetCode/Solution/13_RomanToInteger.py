class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M':1000, 'D':500, 'C':100, 'L': 50, 'X':10,'V':5,'I':1}
        result = 0
        length = len(s)
        for i in range (0,length-1):
            if roman[s[i]] < roman[s[i+1]]:
                result = result - roman[s[i]]
            if roman[s[i]] >= roman[s[i+1]]:
                result = result + roman[s[i]]
        return result+roman[s[-1]]


def execute():
    num = 'MMIX'
    sol = Solution()
    print(sol.romanToInt(num))


if __name__=="__main__":
    execute()