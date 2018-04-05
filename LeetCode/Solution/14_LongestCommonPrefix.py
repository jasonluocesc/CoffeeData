class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        strs.sort(key=len)

        if len(strs[0]) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        first = strs[0]
        last = strs[-1]
        length = len(first)
        i=0
        while i<length:
            if first[i]==last[i]:
                for str in strs:
                    if str[i] == first[i]:
                        pass
                    else:
                        return first[0:i]
                i+=1
            else:
                return first[0:i]
        return first[0:i]




strs_1 = ["abab","aba","abc"]
#strs_1.sort(key=len)
#print(strs_1)
print(Solution().longestCommonPrefix(strs_1))
