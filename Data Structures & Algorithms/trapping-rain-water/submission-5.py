class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
            
        maxIdx = 0
        for i in range(len(height)):
            if height[i] > height[maxIdx]:
                maxIdx = i

        area = 0
        # left to right pass up to highest point
        l, r = 0, 1
        while (r < len(height) and r <= maxIdx):
            if height[l] > height[r]:
                r += 1
                continue
            # closed area --> calculate area
            maxHeight = min(height[l], height[r])
            for i in range(l + 1, r):
                area += maxHeight - height[i]

            l, r = r, r + 1
        # right to left pass up to highest point
        l, r = len(height) - 2, len(height) - 1
        while (l > -1 and l >= maxIdx):
            if height[r] > height[l]:
                l -= 1
                continue
            # closed area --> calculate area
            maxHeight = min(height[l], height[r])
            for i in range(l + 1, r):
                area += maxHeight - height[i]
            
            r, l = l, l - 1

        return area
