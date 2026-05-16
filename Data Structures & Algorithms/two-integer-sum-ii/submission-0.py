class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while (l < r):
            if (numbers[l] + numbers[r] == target):
                return [l + 1, r + 1]
            if (target - numbers[r]) < numbers[l]:
                r -= 1
            elif (target - numbers[l]) > numbers[r]:
                l += 1
