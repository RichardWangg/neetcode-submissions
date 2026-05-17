class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        vectors = [(position[i], speed[i]) for i in range(n)]
        vectors = sorted(vectors, key = lambda v: v[0])
        stack = [vectors[n - 1]] # stack (pos, speed)

        for i in range(n - 2, -1, -1):
            # Check if it can merge with fleet directly ahead of it, if not its a new fleet
            fleetPos, fleetSpeed = stack[-1]
            currPos, currSpeed = vectors[i]
            numer = currPos - fleetPos
            denom = fleetSpeed - currSpeed
            
            interceptTime = -1 if denom == 0 else numer / denom
            interceptPos = currSpeed*interceptTime + currPos
            fleetTargetTime = (target - fleetPos) / fleetSpeed
            isMerge = interceptPos <= target and interceptTime <= fleetTargetTime and interceptTime > 0

            if not isMerge:
                stack.append((currPos, currSpeed)) # new fleet
        
        return len(stack)
