class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # This checks for valid rows and columns
        validC = []
        for i in range(9):
            validC.append(set())
        for r in range(len(board)):
            validR = set()
            for c in range(len(board[0])): 
                value = board[r][c]
                if value == ".":
                    continue
                if value in validR or value in validC[c]:
                   return False 
                validC[c].add(value)
                validR.add(value) 
        
        # This checks for the sub grids
        for i in range(9):
            validG = set()
            for r in range(3):
                for c in range(3):
                    row = (i // 3) * 3 + r 
                    col = (i % 3) * 3 + c

                    value = board[row][col]

                    if value == ".":
                        continue
                    if value in validG:
                        return False
                    validG.add(value)

        return True