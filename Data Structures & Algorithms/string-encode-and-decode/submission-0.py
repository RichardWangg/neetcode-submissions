class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = [f'{len(strs)}T']
        for s in strs:
            prefix = f'{len(s)}x'
            msg.append(prefix+s)
        return ''.join(msg)

    def decode(self, s: str) -> List[str]:
        res = []
        # get total words prefix
        idx = 0
        wordsPrefix = ''
        while (s[idx] != 'T'):
            wordsPrefix += s[idx]
            idx += 1
        idx += 1
        words = int(wordsPrefix)
        # get length prefix and extract word
        for i in range(words):
            lenPrefix = ''
            while (s[idx] != 'x'):
                lenPrefix += s[idx]
                idx += 1
            idx += 1
            length = int(lenPrefix)
            word = ''
            for i in range(length):
                word += s[idx]
                idx += 1
            res.append(word)
        
        return res

