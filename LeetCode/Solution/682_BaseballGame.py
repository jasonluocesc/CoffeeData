class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        points = []

        for op in ops:
            if op == 'C':
                points.pop()
            elif op == 'D':
                d = points[-1]*2
                points.append(d)
            elif op == '+':
                temp = points[-1]+points[-2]
                points.append(temp)
            else:
                points.append(int(op))

        return sum(points)

opss = ["5","2","C","D","+"]
print(Solution().calPoints(opss))