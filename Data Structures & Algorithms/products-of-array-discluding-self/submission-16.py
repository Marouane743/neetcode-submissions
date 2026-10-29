class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        p = 1
        for i, x in enumerate(nums):
            res[i] = p
            p *= x

        p = 1
        for i, x in enumerate(reversed(nums)):
            j = n - 1 - i
            res[j] *= p
            p *= x

        return res