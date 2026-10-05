class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = []
        for i in range(9):
            for j in range(9):
                key = board[i][j]
                if key != '.':
                
                    row_key =(key,i)
                    col_key = (j,key)
                    box_key = (i//3,j//3,key)

                    if row_key in seen or col_key in seen or box_key in seen:
                        return False
                    seen.append(row_key)
                    seen.append(box_key)
                    seen.append(col_key)
        return True

        