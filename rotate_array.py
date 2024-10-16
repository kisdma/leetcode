class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if k % N == 0:
            return
        if 2 * k == N:
            for ind in range(N // 2):
                temp = nums[(k + ind) % N]
                nums[(k + ind) % N] = nums[ind]
                nums[ind] = temp
        else:
            temp = nums[- k % N]
            ind = 0
            print(ind, temp)
            for _ in range(N):
                temp1 = nums[ind]
                nums[ind] = temp
                temp = temp1
                ind = (k + ind) % N
                print(ind, temp, nums)
