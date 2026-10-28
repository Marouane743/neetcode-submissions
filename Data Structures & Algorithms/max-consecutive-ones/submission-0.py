class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        a = 0
        L = []
        for i in range(n):
            if nums[i] == 1 :
                a += 1
            if (nums[i] == 0) or (i == n-1) :
                L.append(a)
                a = 0
            
        return max(L)

        