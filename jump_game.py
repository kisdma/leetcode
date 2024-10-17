class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        zero_ind = len(nums) - 1
        zero_flag = False
        cant_jump_over = False
        zero_count = 0
        nonzero_flag = True
        for ind1 in range(len(nums)-2, -1, -1):
            if nums[ind1] == 0:
                if nonzero_flag:
                    zero_count = 0
                    nonzero_flag = False
                else:
                    zero_count += 1
                if cant_jump_over:
                    return False
                cant_jump_over = True
                zero_ind = ind1
                zero_flag = True
            elif zero_flag:
                nonzero_flag = True
                if nums[ind1] > zero_ind - ind1 + zero_count:
                    cant_jump_over = False
            print(zero_ind, zero_flag, cant_jump_over, zero_count)
        return not cant_jump_over