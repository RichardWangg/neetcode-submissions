import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        freqList = [[] for i in range(len(nums) + 1)]
        for key, val in count.items():
            freqList[val].append(key)

        output = []
        for i in range(len(nums), -1, -1):
            for num in freqList[i]:
                output.append(num)
                k -= 1
            if (k == 0):
                return output
        
        return 0
        



