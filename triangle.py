class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        if N == 1:
            return triangle[0][0]
        if N == 2:
            return triangle[0][0] + min(triangle[1])
        up_to_level = [0] * N
        up_to_level[0] = triangle[0][0]
        for ind in range(1, N):
            temp = up_to_level[0]
            for ind1 in range(1, ind):
                temp1 = up_to_level[ind1]
                up_to_level[ind1] = min(temp, up_to_level[ind1]) + triangle[ind][ind1]
                temp = temp1
            up_to_level[0] = up_to_level[0] + triangle[ind][0]
            up_to_level[ind] = temp + triangle[ind][-1]
        return min(up_to_level)