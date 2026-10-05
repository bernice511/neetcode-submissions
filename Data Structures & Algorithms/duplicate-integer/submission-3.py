class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)
            print(freq[num])
            if freq[num]==1:
                return True
            else:
                freq[num] = 1
        return False