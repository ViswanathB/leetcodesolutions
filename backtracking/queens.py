from typing import List


class Solution:
    def printMatrix(self, matrix: List[List[int]]):
        for row in range(0, len(matrix)):
            print("[", end="")
            for col in range(0, len(matrix[0])):
                print(matrix[row][col], end=",")
            print("]")

    def IsMatrixValid(self, matrix: List[List[int]], current_row: int, current_col: int) -> bool:
        print(f"Checking at {current_row}, {current_col}")
        self.printMatrix(matrix)
        n = len(matrix)

        for i in range(0, n):
            if i == current_row:
                continue

            if matrix[i][current_col]:
                print(f"Failed at {i}, {current_col}")
                return False

        start_diag_row = current_row - min(current_row, current_col)
        start_diag_col = current_col - min(current_row, current_col)

        while start_diag_row < n and start_diag_col < n:
            if start_diag_row == current_row and start_diag_col == current_col:
                start_diag_row += 1
                start_diag_col += 1
                continue

            if matrix[start_diag_row][start_diag_col]:
                print(f"Failed at {start_diag_row}, {start_diag_col}")
                return False

            start_diag_row += 1
            start_diag_col += 1

        # Other diag
        start_diag_row = current_row
        start_diag_col = current_col

        while start_diag_row > 0 and start_diag_col < n - 1:
            start_diag_row -= 1
            start_diag_col += 1

        while start_diag_row < n and start_diag_col >= 0:
            if start_diag_row == current_row and start_diag_col == current_col:
                start_diag_row += 1
                start_diag_col -= 1
                continue

            if matrix[start_diag_row][start_diag_col]:
                print(f"Failed at {start_diag_row}, {start_diag_col}")
                return False

            start_diag_row += 1
            start_diag_col -= 1

        return True

    def startFilling(self, current_row: int, n: int, matrix: List[List[int]]):
        print(f"Currently filling {current_row}")
        if current_row == n:
            self.result += 1
            return

        for i in range(0, n):
            matrix[current_row][i] = True

            if self.IsMatrixValid(matrix, current_row, i):
                self.startFilling(current_row + 1, n, matrix)

            matrix[current_row][i] = False

    def totalNQueens(self, n: int) -> int:
        self.result = 0

        row = [False for i in range(0, n)]
        matrix = [row.copy() for i in range(0, n)]

        self.startFilling(0, n, matrix)
        return self.result


print(Solution().totalNQueens(5))
