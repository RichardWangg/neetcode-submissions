class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        seen = set()
        seqs = {}

        for num in nums:
            if num in seen:
                continue
            
            seqs[num] = 1
            seen.add(num)
            curr = num
            while (curr + 1 in nums):
                seqs[num] += 1
                curr += 1
                seen.add(curr)
        
        res = 0
        for val in seqs.values():
            res = max(res, val)
        
        return res