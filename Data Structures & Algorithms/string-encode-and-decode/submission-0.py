class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ''
        for s in strs:
            r += str(len(s)) + '#' + s
        return r

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            print(j)
            length = int(s[i:j])
            start=j+1
            end=start+length
            print(end)
            res.append(s[start:end])

            i=end
        return res



