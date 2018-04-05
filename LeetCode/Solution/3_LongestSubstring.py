class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlength,temp=1,1
        left, right = 0,0
        if not s:
            return 0
        elif len(s)==1:
            return maxlength
        else:
            for i in range(0,len(s)-1):
                pass


print(Solution().lengthOfLongestSubstring("wwwkew"))