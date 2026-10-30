class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        M = [[] for i in range(n)]
        D = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if board[i][j] != "." :
                    D[board[i][j]].append((i,j))
        L = list(D.values())
        for R in L:
            r = len(R)
            if  r > 9 : 
                return False
            rows,cols = zip(*R)
            if len(set(rows)) != len(rows) : return False
            if len(set(cols)) != len(cols) : return False
            box = [(x[0]//3,x[1]//3) for x in R]
            if len(set(box)) != len(box) : return False
                
        return True
             
        