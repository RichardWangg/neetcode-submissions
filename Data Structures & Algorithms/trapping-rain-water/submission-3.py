class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        # find start and stop points, remove cases of leading and trailing zeros
        start, stop = 0, len(height) - 1
        while (start < len(height) and height[start] == 0):
            start += 1
        while (stop > 0 and height[stop] == 0):
            stop -= 1
            
        maxIdx = 0
        for i in range(len(height)):
            if height[i] > height[maxIdx]:
                maxIdx = i

        area = 0
        # left to right pass up to highest point
        l, r = start, start + 1
        while (r <= stop and r <= maxIdx):
            if height[l] > height[r]:
                r += 1
                continue
            # closed area --> calculate area
            maxHeight = min(height[l], height[r])
            for i in range(l + 1, r):
                h = maxHeight - height[i]
                w = 1
                area += h*w

            l, r = r, r + 1
        # right to left pass up to highest point
        l, r = stop - 1, stop
        while (l >= start and l >= maxIdx):
            if height[r] > height[l]:
                l -= 1
                continue
            # closed area --> calculate area
            maxHeight = min(height[l], height[r])
            for i in range(l + 1, r):
                h = maxHeight - height[i]
                w = 1
                area += h*w
            
            r, l = l, l - 1

        return area
