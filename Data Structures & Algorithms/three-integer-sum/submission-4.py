class Solution:
    def twoSum(self, nums, l, r, target):
        pairs = []
        while (l < r):
            if (nums[l] + nums[r] == target):
                pairs.append([nums[l], nums[r]])
                l += 1
                r -= 1
            if (target - nums[r]) < nums[l]:
                r -= 1
            elif (target - nums[l]) > nums[r]:
                l += 1
        return pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        if nums[0] > 0:
            return []
        
        triplets = set()
        for i in range(len(nums)):
            pairs = self.twoSum(nums, i + 1, len(nums) - 1, -1*nums[i])
            if len(pairs) > 0:
                pairs = [pair + [nums[i]] for pair in pairs]
                for pair in pairs:
                    triplets.add(tuple(sorted(pair)))
        
        return [list(triplet) for triplet in triplets]

         