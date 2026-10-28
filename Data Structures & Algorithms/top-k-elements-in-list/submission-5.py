class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D = defaultdict(int)
        a = 0 
        for s in nums :
            D[s] = 0
        for s in nums :
            D[s] +=1
        n = len(nums)
        L = [[] for i in range(n+1)]
        for x in D.items() : 
            L[x[1]].append(x[0])
        R = []
        m = len(L)
        for i in range(m-1,-1,-1):
            if L[i] :
                R = R + L[i]
                if len(R) >= k : 
                    return R[:k]
                    
        return R



        