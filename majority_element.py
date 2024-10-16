class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        for ind in range(1, len(nums)):
            if nums[ind] == candidate:
                count += 1
            else:
                if count == 0:
                    candidate = nums[ind]
                else:
                    count -= 1
        return candidate
    
print(Solution().majorityElement(nums=[6,4,6,1,6,6,7,7,6,6]))
print(Solution().majorityElement(nums=[1,3,1,1,4,1,1,5,1,1,6,2,2]))
print(Solution().majorityElement(nums=[8,8,7,7,7]))
print(Solution().majorityElement(nums=[6,6,6,6,7,7,7]))