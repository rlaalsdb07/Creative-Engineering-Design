"""틱택토 — 담당: 팀원 E

[규칙]
- 2명이 번갈아 X, O 를 3x3 판에 놓는다.
- 가로·세로·대각선으로 세 칸을 먼저 채우면 승리, 판이 가득 차면 무승부.

[구현 힌트]
- check_winner(board: list[list[str]]) -> str | None   # "X" | "O" | None
- is_full(board: list[list[str]]) -> bool
"""

import utils

GAME_NAME = "틱택토"


def create_board() -> list[list[str]]:
    """3x3 크기의 빈 보드를 생성한다."""
    return [[" " for _ in range(3)] for _ in range(3)]


def format_board(board: list[list[str]]) -> str:
    """보드를 문자열로 보기 좋게 렌더링한다."""
    lines = []
    for r in range(3):
        row_str = " | ".join(
            board[r][c] if board[r][c] != " " else str(r * 3 + c + 1) for c in range(3)
        )
        lines.append(f" {row_str} ")
        if r < 2:
            lines.append("---+---+---")
    return "\n".join(lines)


def print_board(board: list[list[str]]) -> None:
    """보드 상태를 출력한다."""
    print("\n" + format_board(board) + "\n")


def check_winner(board: list[list[str]]) -> str | None:
    """승자가 있으면 'X' 또는 'O'를 반환하고, 없으면 None을 반환한다."""
    # 가로 확인
    for r in range(3):
        if board[r][0] != " " and board[r][0] == board[r][1] == board[r][2]:
            return board[r][0]

    # 세로 확인
    for c in range(3):
        if board[0][c] != " " and board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]

    # 대각선 확인
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None


def is_full(board: list[list[str]]) -> bool:
    """보드가 빈 칸 없이 가득 찼는지 확인한다."""
    for row in board:
        if " " in row:
            return False
    return True


def make_move(board: list[list[str]], pos: int, player: str) -> bool:
    """1~9 위치에 player('X' 또는 'O')의 돌을 놓는다. 성공 시 True를 반환한다."""
    if pos < 1 or pos > 9:
        return False
    row = (pos - 1) // 3
    col = (pos - 1) % 3
    if board[row][col] != " ":
        return False
    board[row][col] = player
    return True


def play() -> None:
    """한 판을 진행한다. 끝나면 return 하여 메인 메뉴로 돌아간다."""
    print("\n=== 틱택토 게임을 시작합니다! ===")
    print("규칙: 두 플레이어가 번갈아가며 1~9 번호 위치에 돌을 놓습니다.")

    while True:
        board = create_board()
        current_player = "X"

        while True:
            print_board(board)
            pos = utils.ask_int(
                f"[{current_player}의 차례] 돌을 놓을 위치를 선택하세요 (1~9): ",
                1,
                9,
            )

            if not make_move(board, pos, current_player):
                print("이미 돌이 놓인 자리입니다. 다른 칸을 선택하세요.")
                continue

            winner = check_winner(board)
            if winner is not None:
                print_board(board)
                print(f"축하합니다! 플레이어 [{winner}]의 승리입니다!")
                break

            if is_full(board):
                print_board(board)
                print("무승부입니다! 모든 칸이 채워졌습니다.")
                break

            current_player = "O" if current_player == "X" else "X"

        if not utils.ask_yes_no("한 판 더 하시겠습니까?"):
            print("틱택토를 종료하고 메인 메뉴로 돌아갑니다.")
            break
