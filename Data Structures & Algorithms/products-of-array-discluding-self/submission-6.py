from math import prod 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        M = nums
        a = len(nums)
        L=[0 for i in range(a)]
        
        b = prod(nums)
        for i in range(a):
            if nums[i] != 0 :
                L[i] = b//nums[i]
            else :
                M = nums[:i]
                M.extend(nums[i+1:])
                L[i] = prod(M)

        return L