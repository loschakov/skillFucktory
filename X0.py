def print_board(board):
    """Выводит игровое поле на экран"""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
        print("\n")


def check_winner(board):
    """Проверяет есть ли победитель или ничья
    :return: 'X', '0', 'Draw', 'None' """

    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # проверка на ничью
    if all(cell != " " for row in board for cell in row):
        return "Draw"

    return None


def main():
    """Основная функция игры"""
    board = [[" " for i in range(3)] for k in range(3)]
    current_player = "X"

    print("Игровое поле пронумеровано от 1 до 9")
    print(" 1 | 2 | 3 \n ---+---+---\n 4 | 5 | 6 \n---+---+---\n 7 | 8 | 9\n")
    print_board(board)

    while True:
        move = int(input(f"Ход игрока {current_player} (1-9): ")) - 1
        if move < 0 or move >= 9:
            print("введите чилос от 1 до 9")
            continue

        row, col = divmod(move, 3)

        if board[row][col] != " ":
            print("клетка занята выберите другую")
            continue

        # делаем ход
        board[row][col] = current_player
        print_board(board)

        # проверяем на победу
        winner = check_winner(board)
        if winner:
            if winner == "Draw":
                print("ничья")
            else:
                print(f"игрок {winner} победил")
            break

        # смена игрока
        current_player = "0" if current_player == "X" else "X"


main()
