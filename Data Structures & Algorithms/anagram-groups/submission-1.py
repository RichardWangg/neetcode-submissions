class Solution:
    def generateKey(self, string):
        key = [0]*26
        for i in range(len(string)):
            pos = ord(string[i]) - ord('a')
            key[pos] += 1
        return tuple(key)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapSorted = {}
        for string in strs:
            key = self.generateKey(string)
            if key not in mapSorted:
                mapSorted[key] = [string]
            else:
                mapSorted[key].append(string)
        
        output = [value for value in mapSorted.values()]
        return output