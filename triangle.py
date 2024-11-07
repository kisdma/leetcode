class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        if N == 1:
            return triangle[0][0]
        def onelayer(level, ind):
            if level < N - 2:
                return triangle[level][ind] + \
                    min(onelayer(level + 1, ind), onelayer(level + 1, ind + 1))
            else:
                return triangle[level][ind] + \
                    min(triangle[level + 1][ind], triangle[level + 1][ind + 1])
        return onelayer(0, 0)