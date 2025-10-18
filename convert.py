class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [""] * numRows
        current_row = 0
        direction = -1  # -1 for moving up, 1 for moving down

        for char in s:
            rows[current_row] += char

            if current_row == 0 or current_row == numRows - 1:
                direction *= -1  # Reverse direction at top or bottom row

            current_row += direction

        return "".join(rows)
