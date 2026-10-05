class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_count = 0
        s = set(nums)
        
        for i in s:
            count = 1
            if i-1 in s:
                continue
            while i+1 in s:
                print(i)
                count+=1
                i+=1
            max_count = max(max_count, count) 
        return max_count
            
        
        
        