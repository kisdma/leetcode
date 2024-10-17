class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        bottleneck_flag = False
        zero_ind = len(nums)
        for ind1 in range(len(nums)-2, -1, -1):
            if bottleneck_flag:
                if nums[ind1] > zero_ind - ind1:
                    bottleneck_flag = False
            elif nums[ind1] == 0:
                bottleneck_flag = True
                zero_ind = ind1
        return not bottleneck_flag