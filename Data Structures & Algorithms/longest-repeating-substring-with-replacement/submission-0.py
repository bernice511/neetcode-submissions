class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        right = 0
        n = len(s)
        max_l=0
        max_freq = 0
        for right in range(n):
            char = s[right]
            freq[char] = freq.get(char,0)+1
            max_freq = max(freq[char], max_freq)
            w = right-left+1
            while w-max_freq>k and left<n:
                freq[s[left]]-=1
                left = left+1
                w = right-left+1
            max_l = max(max_l, w)
        return max_l


                
