class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n,L = len(nums),[]
        nums_sorted = sorted(enumerate(nums), key = lambda x : x[1])
        nums_sorted = list(nums_sorted)

        for i in range(n-1):
            for j in range(i+1,n) : 
                if nums_sorted[i][1] + nums_sorted[j][1] == target :
                    L = [nums_sorted[i][0],nums_sorted[j][0]]
                    break
        L = sorted(L)
        return L

        