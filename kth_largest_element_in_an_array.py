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

        start_ind = len(nums)
        end_ind = len(nums) >> 1
        for ind in range(start_ind, end_ind, -1):
            sort_branch(nums, ind)

        not_sorted_flag = True
        while not_sorted_flag:
            start_ind = len(nums) - 1
            # end_ind = ((len(nums) + 1) >> 1) - 2
            end_ind = 0
            print(nums[end_ind + 1:start_ind+1])
            for ind in range(start_ind, end_ind, -1):
                if nums[ind - 1] < nums[ind]:
                    temp = nums[ind - 1]
                    nums[ind - 1] = nums[ind]
                    nums[ind] = temp
                    sort_branch(nums, ind)
                    sort_branch(nums, ind + 1)
                    break
            else:
                not_sorted_flag = False

        ind = len(nums)
        while ind > 0:
            print(nums[ind - 1])
            ind = ind >> 1

        print(nums)
        return nums[k-1]