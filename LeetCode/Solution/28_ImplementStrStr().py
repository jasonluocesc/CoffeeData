class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        index = 0
        if needle in haystack:
            length_n = len(needle)
            c = needle[0]
            for ch in haystack:
                if ch == c:
                    if haystack[index:index+length_n] == needle:
                        return index
                index += 1

        return -1

print(Solution().strStr("aaaaa","bba"))