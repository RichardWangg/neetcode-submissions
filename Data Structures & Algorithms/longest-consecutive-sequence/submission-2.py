class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for num in nums:
            if num - 1 in nums:
                continue
            
            length = 1
            curr = num

            while (curr + 1 in nums):
                length += 1
                curr += 1
            res = max(res, length)
        
        return res