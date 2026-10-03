class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for n in nums:
            map[n] = map.get(n, 0) + 1
        
        sorted_map = dict(sorted(map.items(), key=lambda x:x[1], reverse=True))
        return list(sorted_map.keys())[:k]
        
