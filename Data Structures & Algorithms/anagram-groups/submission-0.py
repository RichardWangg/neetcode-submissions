class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapSorted = {}
        for string in strs:
            stringSorted = ''.join(sorted(string))
            if stringSorted not in mapSorted:
                mapSorted[stringSorted] = [string]
            else:
                mapSorted[stringSorted].append(string)
        
        output = [value for value in mapSorted.values()]
        return output