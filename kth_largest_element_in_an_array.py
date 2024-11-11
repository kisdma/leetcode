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
            if nums[(ind >> 1) - 1] >= nums[ind - 1]:
                return
            if nums[0] < nums[ind - 1]:
                move_branch(nums, ind, ind.bit_length() - 1)
                return
            intervals = (ind.bit_length() - 2) >> 1
            pos = intervals
            while intervals > 0:
                if nums[(ind >> (pos + 1)) - 1] >= nums[ind - 1]:
                    intervals = intervals >> 1
                    pos -= intervals
                else:
                    intervals = (intervals >> 1) + (intervals & 1)
                    pos += intervals
                if pos < 0:
                    move_branch(nums, ind, 1)
                    return
            if nums[(ind >> (pos + 1)) - 1] >= nums[ind - 1]:
                move_branch(nums, ind, pos)
                return
            else:
                move_branch(nums, ind, pos + 1)
                return
        def move_branch(nums, ind, n):
            # print(nums, ind, n)
            temp = nums[ind - 1]
            for i in range(n):
                ind1 = ind >> 1
                nums[ind - 1] = nums[ind1 - 1]
                ind = ind1
            nums[ind - 1] = temp
            return

        # ind = len(nums)
        # while ind > 0:
        #     print(nums[ind - 1])
        #     ind = ind >> 1
        # print('------')

        for ind in range(1, len(nums)):
            sort_branch(nums, ind)

        not_sorted_flag = True
        while not_sorted_flag:
            start_ind = len(nums) - 1
            # end_ind = ((len(nums) + 1) >> 1) - 2
            end_ind = max(((k - 1) >> 1) - 2, 0)
            # print(nums[end_ind + 1:start_ind+1])
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

        # ind = len(nums)
        # while ind > 0:
        #     print(nums[ind - 1])
        #     ind = ind >> 1

        print(nums)
        return nums[k-1]