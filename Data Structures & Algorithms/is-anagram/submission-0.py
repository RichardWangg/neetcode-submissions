class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        count1 = {}
        count2 = {}

        for i in range(len(s)):
            if s[i] not in count1:
                count1[s[i]] = 1
            else:
                count1[s[i]] += 1
            if t[i] not in count2:
                count2[t[i]] = 1
            else:
                count2[t[i]] += 1

        if (count1.keys() != count2.keys()):
            return False

        for key in count1.keys():
            if (count1[key] != count2[key]):
                return False

        return True     