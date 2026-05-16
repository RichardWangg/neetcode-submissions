class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        pairs = []

        while (l < r):
            if (numbers[l] + numbers[r] == target):
                pairs.append([numbers[l], numbers[r]])
                l += 1
                r -= 1
            if (target - numbers[r]) < numbers[l]:
                r -= 1
            elif (target - numbers[l]) > numbers[r]:
                l += 1

        return pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        if nums[0] > 0:
            return []
        
        triplets = set()
        for i in range(len(nums)):
            numbers = []
            if (i == len(nums) - 1):
                numbers = nums[:i]
            else:
                numbers = nums[:i] + nums[i+1:]
    
            pairs = self.twoSum(numbers, -1*nums[i])
            if len(pairs) > 0:
                pairs = [pair + [nums[i]] for pair in pairs]
                for pair in pairs:
                    triplets.add(tuple(sorted(pair)))
        
        return [list(triplet) for triplet in triplets]

         