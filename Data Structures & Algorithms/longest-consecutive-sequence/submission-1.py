class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        seen = set()
        res = 0

        for num in nums:
            if num in seen:
                continue
            
            length = 1
            seen.add(num)
            curr = num

            while (curr + 1 in nums):
                length += 1
                curr += 1
                seen.add(curr)

            res = max(res, length)
        
        return res