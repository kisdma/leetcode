class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] > 0:
            if len(nums)-1 <= nums[0]:
                return True
            for ind2 in range(1, nums[0]+1):
                if self.canJump(nums[ind2:]):
                    return True
        return False