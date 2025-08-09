def main():
    y_max, x_max  = map(int,input().split())

    board = []
    for i in range(y_max):
        row = list(input())
        board.append(row)

    correct_boards = []
    for start_color in ["B", "W"]:
        pattern = []
        for i in range(8):
            row = []
            for j in range(8):
                if (i + j) % 2 == 0:
                    row.append(start_color)
                else:
                    row.append("W" if start_color == "B" else "B")
            pattern.append(row)
        correct_boards.append(pattern)

    min_fixes = float('inf')

    for y_count in range(y_max - 7):
        for x_count in range(x_max - 7):
            cut_board = [row[x_count:x_count+8] for row in board[y_count:y_count+8]]
            for correct_board in correct_boards:
                fixes = sum(
                    1
                    for y in range(8)
                    for x in range(8)
                    if cut_board[y][x] != correct_board[y][x]
                )
                min_fixes = min(min_fixes, fixes)

    print(min_fixes)
            
main()