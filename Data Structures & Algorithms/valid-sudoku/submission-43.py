class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        '''
        each box will have 
        '''

        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)

        for i in range(9):
            for j in range(9):
                number = board[i][j]

                if number == ".":
                    continue
                if number in rows[i]:
                    return False
                elif number in cols[j]:
                    return False
                elif number in squares[(i // 3, j // 3)]:
                    return False
                
                else:
                    rows[i].append(number)
                    cols[j].append(number)
                    squares[(i // 3, j // 3)].append(number)
                
        
        return True

                
                

                

        