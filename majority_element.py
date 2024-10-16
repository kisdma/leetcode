class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def argmin(a):
            return min(range(len(a)), key=lambda x : a[x])
        def argmax(a):
            return max(range(len(a)), key=lambda x : a[x])
        
        if len(nums) in [1, 2]:
            return nums[0]
        if len(nums) == 3:
            candidate = nums[0]
            if candidate == nums[1]:
                return candidate
            else:
                return nums[2]
        smaller = argmin(nums[:3])
        larger = argmax(nums[:3])
        for ind in range(3):
            if ind != smaller and ind != larger:
                candidate = nums[ind]
        smaller = nums[smaller]
        larger = nums[larger]
        smaller_count = 1
        larger_count = 1
        if candidate == larger:
            larger_count += 1
        if smaller == larger:
            larger_count += 1
            smaller_count += 1
        if candidate == smaller:
            smaller_count += 1
        for ind in range(3, len(nums)):
            if smaller == nums[ind]:
                smaller_count += 1
            if smaller < nums[ind] and nums[ind] <= candidate:
                smaller_count -= 1
                if smaller_count <= 1:
                    smaller = nums[ind]
                    smaller_count = 0
            if larger == nums[ind]:
                larger_count += 1
            if larger > nums[ind] and nums[ind] >= candidate:
                larger_count -= 1
                if larger_count <= 1:
                    larger = nums[ind]
                    larger_count = 1
            if smaller > nums[ind]:
                candidate = smaller
                smaller_count -= 1
                if smaller_count <= 1:
                    smaller = nums[ind]
                    smaller_count = 0
            if larger < nums[ind]:
                candidate = larger
                larger_count -= 1
                if larger_count <= 1:
                    larger = nums[ind]
                    larger_count = 1
            if larger_count > smaller_count:
                candidate = larger
            if smaller_count > larger_count:
                candidate = smaller
        return candidate