class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L = [1] * n

        left = 1
        for i in range(n):
            L[i] = left
            left *= nums[i]

        right = 1
        for i in range(n - 1, -1, -1):
            L[i] *= right
            right *= nums[i]

        return L