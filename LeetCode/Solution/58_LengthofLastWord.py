class Solution:
    def lengthOfLastWord(self,s):
        words = s.split()

        if len(words)<1:
            return 0
        else:
            return len(words[-1])

print(Solution().lengthOfLastWord("aaa asdda"))