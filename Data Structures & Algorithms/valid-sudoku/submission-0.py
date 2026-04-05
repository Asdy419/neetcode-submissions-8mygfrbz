class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check all rows
        for i, row in enumerate(board):
            settified = []
            for i in row:
                if i != ".":
                    settified.append(int(i))

            if sorted(list(set(settified))) != sorted(settified):
                return False

        # Check all columns
        for i in range(9):
            settified = []
            for j in range(9):
                if board[j][i] != ".":
                    settified.append(int(board[j][i]))
            
            if sorted(list(set(settified))) != sorted(settified):
                return False


        # Check all 3x3 boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                settified = []
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        if board[i][j] != ".":
                            settified.append(board[i][j])

                if sorted(list(set(settified))) != sorted(settified):
                    return False

        return True

        print(items, row_check)