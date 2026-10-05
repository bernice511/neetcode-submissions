class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def count_letters(s):
        #     count = {}
        #     for char in s:
        #         count[char] = count.get(char,0) + 1
        #     return count
        
        # maps = {}
        # for s in strs:
        #     count = count_letters(s)
        #     maps[tuple(sorted(count.items()))] = maps.get(tuple(sorted(count.items())),[])+[s]
        
        # return [y for x,y in maps.items()]

        sort = {}
        for s in strs:
            sorted_str = "".join(sorted(s))
            sort[sorted_str] = sort.get(sorted_str,[]) + [s]
            # print(sort.values())
        return list(sort.values())