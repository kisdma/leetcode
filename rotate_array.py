class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if k % N == 0:
            return
        ind_ini = 0
        ind = ind_ini
        temp = nums[(ind - k) % N]
        for _ in range(N):
            temp1 = nums[ind]
            nums[ind] = temp
            temp = temp1
            ind = (k + ind) % N
            if ind == ind_ini:
                ind_ini += 1
                ind = ind_ini
                temp = nums[(ind - k) % N]
