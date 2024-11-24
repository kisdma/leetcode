class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for ind in range((n >> 1) - 1, -1, -1):
            ind_parent = ind
            ind_child = ind_parent*2 + 1
            while ind_child < n:
                largest = ind_parent
                if ind_child + 1 < n:
                    if nums[ind_parent] < nums[ind_child + 1]:
                        largest = ind_child + 1
                if nums[largest] < nums[ind_child]:
                    largest = ind_child
                if largest != ind_parent:
                    nums[ind_parent], nums[largest] = nums[largest], nums[ind_parent]
                    ind_parent = largest
                    ind_child = ind_parent*2 + 1
                else:
                    ind_child = n
        for ind in range(len(nums) - 1, len(nums) - k, -1):
            nums[0], nums[ind] = nums[ind], nums[0]
            ind_parent = 0
            ind_child = ind_parent*2 + 1
            while ind_child < ind:
                largest = ind_parent
                if ind_child + 1 < ind:
                    if nums[ind_parent] < nums[ind_child + 1]:
                        largest = ind_child + 1
                if nums[largest] < nums[ind_child]:
                    largest = ind_child
                if largest != ind_parent:
                    nums[ind_parent], nums[largest] = nums[largest], nums[ind_parent]
                    ind_parent = largest
                    ind_child = ind_parent*2 + 1
                else:
                    ind_child = ind
        return nums[0]