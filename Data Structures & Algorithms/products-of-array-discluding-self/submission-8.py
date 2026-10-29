class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L = [0] * n

        b = 1
        zeros = 0

        for x in nums:
            if x == 0:
                zeros += 1
            else:
                b *= x

        if zeros >= 2:
            return L

        for i in range(n):
            if zeros == 1:
                if nums[i] == 0:
                    L[i] = b
            else:
                L[i] = b // nums[i]

        return L
        