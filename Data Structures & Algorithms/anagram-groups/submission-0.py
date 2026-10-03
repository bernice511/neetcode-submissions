class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for text in strs:
            lst = tuple(self.letterCount(text))
            seen[lst].append(text)
        return list(seen.values())
        
    def letterCount(self,text):
        lst = [0] * 26
        for char in text:
            lst[ord(char)-ord('a')]+=1
        return lst