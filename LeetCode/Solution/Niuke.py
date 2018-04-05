class Solution:
    def coding(this, string):
        #string = str(s)
        length = len(string)
        ls = list(string)
        temp = 25 * 25 * 25 + 25 * 25 + 25 + 1
        if length == 0:
            return None
        elif length == 1:
            return int(ord(ls[0]) - ord('a')) * temp
        elif length == 2:
            return int(ord(ls[0]) - ord('a')) * temp + int(ord(ls[1]) - ord('a'))*(25*25+25+1) + 1
        elif length == 3:
            return int(ord(ls[0]) - ord('a')) * temp + int(ord(ls[1]) - ord('a')) * (25*25 +25+ 1) + int(ord(ls[2]) - ord('a'))*(25+1) + 2
        elif length == 4:
            return int(ord(ls[0]) - ord('a')) * temp + int(ord(ls[1]) - ord('a')) * (25 * 25 + 25 + 1) + \
                   int(ord(ls[2]) - ord('a')) * (25 + 1) + int(ord(ls[3]) - ord('a')) + 3
print(Solution().coding('qqq'))