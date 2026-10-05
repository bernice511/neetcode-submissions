class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for n in nums:
            seen[n] = seen.get(n,0)+1
        sort = dict(sorted(seen.items(), key=lambda item: item[1], reverse=True))
        for i in range(k):
            return list(sort)[:k]
        
