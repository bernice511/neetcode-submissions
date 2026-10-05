class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]*len(nums)

        for i in range(1,len(nums)):
            pref[i] = pref[i-1]*nums[i-1]

        suf = 1
        for i in range(len(nums)-1, -1, -1):
            pref[i] = pref[i]*suf
            suf*=nums[i]
        return pref
            


        