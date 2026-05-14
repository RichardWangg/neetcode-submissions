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

        index = len(nums)
        output = []
        while (k > 0): 
            while (len(freqList[index]) == 0):
                index -= 1
            for num in freqList[index]:
                output.append(num)
                k -= 1
            freqList[index] = []
        
        return output
        



