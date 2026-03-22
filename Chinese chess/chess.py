# 中国象棋游戏
# 简化的命令行版本

import copy

# 棋子类型
PIECES = {
    'r': '车', 'n': '马', 'b': '象', 'a': '士', 'k': '帅', 'c': '炮', 'p': '兵',
    'R': '车', 'N': '马', 'B': '象', 'A': '士', 'K': '帅', 'C': '炮', 'P': '兵'
}

# 初始棋盘布局 (红方在底部，黑方在顶部)
INITIAL_BOARD = [
    ['r', 'n', 'b', 'a', 'k', 'a', 'b', 'n', 'r'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', 'c', '.', '.', '.', '.', '.', 'c', '.'],
    ['p', '.', 'p', '.', 'p', '.', 'p', '.', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', '.', 'P', '.', 'P', '.', 'P', '.', 'P'],
    ['.', 'C', '.', '.', '.', '.', '.', 'C', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['R', 'N', 'B', 'A', 'K', 'A', 'B', 'N', 'R']
]

class ChessPiece:
    def __init__(self, piece_type, color):
        self.type = piece_type.lower()
        self.color = color  # 'red' or 'black'
        self.symbol = piece_type

    def __str__(self):
        return PIECES[self.symbol]

class ChineseChess:
    def __init__(self):
        self.board = [[None for _ in range(9)] for _ in range(10)]
        self.current_player = 'red'  # 红方先走
        self.setup_board()

    def setup_board(self):
        for row in range(10):
            for col in range(9):
                piece = INITIAL_BOARD[row][col]
                if piece != '.':
                    color = 'black' if piece.islower() else 'red'
                    self.board[row][col] = ChessPiece(piece, color)

    def print_board(self):
        print("  0 1 2 3 4 5 6 7 8")
        for i, row in enumerate(self.board):
            print(f"{i}", end=" ")
            for cell in row:
                if cell:
                    print(cell, end=" ")
                else:
                    print(".", end=" ")
            print()

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        if not (0 <= start_row < 10 and 0 <= start_col < 9 and 0 <= end_row < 10 and 0 <= end_col < 9):
            return False
        piece = self.board[start_row][start_col]
        if not piece or piece.color != self.current_player:
            return False
        target = self.board[end_row][end_col]
        if target and target.color == self.current_player:
            return False

        # 简单的移动验证 (这里简化了，实际需要更复杂的规则)
        if piece.type == 'r':  # 车
            if start_row == end_row:
                step = 1 if end_col > start_col else -1
                for col in range(start_col + step, end_col, step):
                    if self.board[start_row][col]:
                        return False
                return True
            elif start_col == end_col:
                step = 1 if end_row > start_row else -1
                for row in range(start_row + step, end_row, step):
                    if self.board[row][start_col]:
                        return False
                return True
        elif piece.type == 'n':  # 马
            row_diff = abs(end_row - start_row)
            col_diff = abs(end_col - start_col)
            if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
                # 检查马腿
                if row_diff == 2:
                    block_row = start_row + (1 if end_row > start_row else -1)
                    if self.board[block_row][start_col]:
                        return False
                else:
                    block_col = start_col + (1 if end_col > start_col else -1)
                    if self.board[start_row][block_col]:
                        return False
                return True
        elif piece.type == 'b':  # 象
            if abs(end_row - start_row) == 2 and abs(end_col - start_col) == 2:
                block_row = start_row + (1 if end_row > start_row else -1)
                block_col = start_col + (1 if end_col > start_col else -1)
                if self.board[block_row][block_col]:
                    return False
                # 象不能过河
                if piece.color == 'red' and end_row < 5:
                    return False
                if piece.color == 'black' and end_row > 4:
                    return False
                return True
        elif piece.type == 'a':  # 士
            if abs(end_row - start_row) == 1 and abs(end_col - start_col) == 1:
                # 士只能在九宫格内
                if piece.color == 'red' and 7 <= end_row <= 9 and 3 <= end_col <= 5:
                    return True
                if piece.color == 'black' and 0 <= end_row <= 2 and 3 <= end_col <= 5:
                    return True
        elif piece.type == 'k':  # 帅
            if abs(end_row - start_row) + abs(end_col - start_col) == 1:
                # 帅只能在九宫格内
                if piece.color == 'red' and 7 <= end_row <= 9 and 3 <= end_col <= 5:
                    return True
                if piece.color == 'black' and 0 <= end_row <= 2 and 3 <= end_col <= 5:
                    return True
        elif piece.type == 'c':  # 炮
            if start_row == end_row:
                pieces_between = 0
                step = 1 if end_col > start_col else -1
                for col in range(start_col + step, end_col, step):
                    if self.board[start_row][col]:
                        pieces_between += 1
                if target:
                    return pieces_between == 1
                else:
                    return pieces_between == 0
            elif start_col == end_col:
                pieces_between = 0
                step = 1 if end_row > start_row else -1
                for row in range(start_row + step, end_row, step):
                    if self.board[row][start_col]:
                        pieces_between += 1
                if target:
                    return pieces_between == 1
                else:
                    return pieces_between == 0
        elif piece.type == 'p':  # 兵
            if piece.color == 'red':
                if end_row > start_row and start_col == end_col:
                    return True
                if end_row == start_row and abs(end_col - start_col) == 1 and start_row > 4:
                    return True
            else:
                if end_row < start_row and start_col == end_col:
                    return True
                if end_row == start_row and abs(end_col - start_col) == 1 and start_row < 5:
                    return True
        return False

    def make_move(self, start_row, start_col, end_row, end_col):
        if self.is_valid_move(start_row, start_col, end_row, end_col):
            self.board[end_row][end_col] = self.board[start_row][start_col]
            self.board[start_row][start_col] = None
            self.current_player = 'black' if self.current_player == 'red' else 'red'
            return True
        return False

    def is_checkmate(self):
        # 简化的将死检查 (实际需要更复杂)
        return False

    def play(self):
        while not self.is_checkmate():
            self.print_board()
            print(f"\n{self.current_player}方轮到你了")
            try:
                start = input("输入起始位置 (行 列): ").split()
                end = input("输入目标位置 (行 列): ").split()
                start_row, start_col = int(start[0]), int(start[1])
                end_row, end_col = int(end[0]), int(end[1])
                if self.make_move(start_row, start_col, end_row, end_col):
                    print("移动成功")
                else:
                    print("无效移动")
            except:
                print("输入错误，请重新输入")

if __name__ == "__main__":
    game = ChineseChess()
    game.play()
