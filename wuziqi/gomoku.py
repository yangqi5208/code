import os

# 五子棋游戏
# 棋盘大小
BOARD_SIZE = 15

# 初始化棋盘
def init_board():
    return [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# 打印棋盘
def print_board(board):
    print('   ' + ' '.join([str(i).rjust(2) for i in range(BOARD_SIZE)]))
    print('  +' + '-' * (BOARD_SIZE * 3 - 1) + '+')
    for i in range(BOARD_SIZE):
        row = f'{i:2d}|'
        for j in range(BOARD_SIZE):
            row += board[i][j] + ' |'
        print(row)
        if i < BOARD_SIZE - 1:
            print('  +' + '-' * (BOARD_SIZE * 3 - 1) + '+')

# 检查获胜
def check_win(board, row, col, player):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dr, dc in directions:
        count = 1
        # 正向
        r, c = row + dr, col + dc
        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
            count += 1
            r += dr
            c += dc
        # 反向
        r, c = row - dr, col - dc
        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
            count += 1
            r -= dr
            c -= dc
        if count >= 5:
            return True
    return False

# 主游戏循环
def main():
    board = init_board()
    players = ['X', 'O']
    turn = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # 清屏
        print_board(board)
        player = players[turn % 2]
        print(f"玩家 {player} 的回合")
        try:
            row = int(input("输入行 (0-14): "))
            col = int(input("输入列 (0-14): "))
            if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
                print("无效坐标，请重新输入。")
                continue
            if board[row][col] != ' ':
                print("该位置已被占用，请重新输入。")
                continue
            board[row][col] = player
            if check_win(board, row, col, player):
                os.system('cls' if os.name == 'nt' else 'clear')
                print_board(board)
                print(f"玩家 {player} 获胜！")
                break
            turn += 1
        except ValueError:
            print("请输入有效的数字。")

if __name__ == "__main__":
    main()