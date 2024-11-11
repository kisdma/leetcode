class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return []
        if k == 1:
            return max(nums)
        if k == len(nums):
            return min(nums)
        def return_sorted_idx():
            pass
        def sort_branch(nums, ind):
            pass
        ind = len(nums)-1
        while ind > 0:
            print(nums[ind - 1])
            ind = ind >> 1