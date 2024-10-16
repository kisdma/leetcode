class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for indk in range(k):
            temp = nums[-1]
            for ind in range(len(nums)):
                temp1 = nums[ind]
                nums[ind] = temp
                temp = temp1