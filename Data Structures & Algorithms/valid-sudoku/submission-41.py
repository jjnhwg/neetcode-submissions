class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #input of a 2d board 
        #output is a boolean value represetning if the board is a valid sudoku 

        '''
        each row doesnt contatin a duplicat
        each column doesnt contain a duplicate
        each 3x3 square doesnt include a duplicate 


        thought process:
        have rows and cols and squares hash map with keys being the row or the column you are at
        iterate thorugh the board checking to see if that board is in the rows and cols 


        important points to consider: 
        the keys for the squares will be the coordinate of whatever square you are on by using 

        i // 3
        j // 3 

        '''

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[i // 3, j // 3]:
                    return False
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[i // 3, j // 3].add(board[i][j])
        
        return True
                
                    

                
                




        