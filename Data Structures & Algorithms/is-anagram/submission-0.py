class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def freq(s):
            freq = {}
            for char in s:
                freq[char] = freq.get(char, 0)+1
            return freq
        
        return freq(s)==freq(t)


        