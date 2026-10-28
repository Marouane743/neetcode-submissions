class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        L = sorted(nums)
        for i in range(n-1) : 
            if L[i] == L[i+1] : 
                return True       
        return False

        