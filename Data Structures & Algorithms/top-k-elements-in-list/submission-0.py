import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        items = list(count.items())
        itemsHeap = [(item[1]*-1, item[0]) for item in items] # heapify works on first index in tuple
        heapq.heapify(itemsHeap)
        print(itemsHeap)

        output = []
        for i in range(k):
            item = heapq.heappop(itemsHeap)
            output.append(item[1])

        return output
