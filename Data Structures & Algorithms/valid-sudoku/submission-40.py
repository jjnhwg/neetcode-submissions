class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''


        '''

        
        #rows 
        for i in range(9):
            seen = set()
            for k in range(9):

                if board[i][k] == ".":
                    continue 
                if board[i][k] in seen:
                    return False
                
                seen.add(board[i][k])
        
        #cols 
        for i in range(9):
            seen = set()
            for k in range(9):
                
                if board[k][i] == ".":
                    continue 
                if board[k][i] in seen:
                    return False
                seen.add(board[k][i])
        
        #square 
        #get the box you are supposed to get and then solve from there 


        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
                
