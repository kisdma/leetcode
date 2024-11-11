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
            not_sorted_flag = True
            while not_sorted_flag:
                h = ind
                while h > 1:
                    h1 = h >> 1
                    if nums[h1 - 1] < nums[h - 1]:
                        temp = nums[h1 - 1]
                        nums[h1 - 1] = nums[h - 1]
                        nums[h - 1] = temp
                        break
                    h = h1
                else:
                    not_sorted_flag = False
        ind = len(nums)
        while ind > 0:
            print(nums[ind - 1])
            ind = ind >> 1
        print('------')
        ind = len(nums)
        sort_branch(nums, ind)
        while ind > 0:
            print(nums[ind - 1])
            ind = ind >> 1