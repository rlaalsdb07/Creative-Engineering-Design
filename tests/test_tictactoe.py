"""틱택토 게임의 순수 함수 단위 테스트 — 작성자: 전민성"""

from games.tictactoe import (
    check_winner,
    create_board,
    format_board,
    is_full,
    make_move,
)


def test_create_board():
    board = create_board()
    assert len(board) == 3
    assert all(len(row) == 3 for row in board)
    assert all(cell == " " for row in board for cell in row)


def test_check_winner_rows():
    board = [
        ["X", "X", "X"],
        ["O", " ", "O"],
        [" ", " ", " "],
    ]
    assert check_winner(board) == "X"


def test_check_winner_cols():
    board = [
        ["O", "X", " "],
        ["O", "X", " "],
        ["O", " ", " "],
    ]
    assert check_winner(board) == "O"


def test_check_winner_diagonals():
    board1 = [
        ["X", "O", " "],
        ["O", "X", " "],
        [" ", " ", "X"],
    ]
    assert check_winner(board1) == "X"

    board2 = [
        [" ", "X", "O"],
        [" ", "O", "X"],
        ["O", " ", " "],
    ]
    assert check_winner(board2) == "O"


def test_check_winner_none():
    board = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", " "],
    ]
    assert check_winner(board) is None


def test_is_full():
    not_full_board = [
        ["X", "O", "X"],
        ["X", " ", "O"],
        ["O", "X", "O"],
    ]
    assert not is_full(not_full_board)

    full_board = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"],
    ]
    assert is_full(full_board)


def test_check_winner_draw():
    """보드가 꽉 찼으나 승자가 없는 무승부 상태 테스트"""
    board = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"],
    ]
    # 1. 승자가 없어야 함 (None)
    assert check_winner(board) is None
    # 2. 보드가 꽉 찬 상태여야 함 (True)
    assert is_full(board) is True


def test_make_move():
    board = create_board()
    assert make_move(board, 1, "X") is True
    assert board[0][0] == "X"

    # 이미 놓인 자리에 다시 놓으려고 할 때
    assert make_move(board, 1, "O") is False
    assert board[0][0] == "X"

    # 범위 밖 위치 테스트
    assert make_move(board, 0, "X") is False
    assert make_move(board, 10, "X") is False


def test_format_board():
    board = create_board()
    board[0][0] = "X"
    formatted = format_board(board)
    assert "X" in formatted
    assert "2" in formatted
    assert "---+---+---" in formatted
