class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line1 = set("qwertyuiop")
        line2 = set("asdfghjkl")
        line3 = set("zxcvbnm")

        result = []
        for word in words:
            test = set(word.lower())
            if test&line1 == test:
                result.append(word)
            elif test&line2 ==test:
                result.append(word)
            elif test&line3 ==test:
                result.append(word)
        return result

k = ["Hello","Alaska","Dad","Peace"]
x =Solution().findWords(k)
print(x)