"""가위바위보 — 담당: 팀원 D

[규칙]
- 컴퓨터와 3판 2선승제로 대결한다.
- 입력: 1(가위) 2(바위) 3(보)

[구현 힌트]
- decide(player: str, computer: str) -> str   # "win" | "lose" | "draw"
"""

GAME_NAME = "가위바위보"


def decide(player: str, computer: str) -> str:
    """Decide the winner of one round."""
    if player == computer:
        return "draw"

    if (
        (player == "1" and computer == "3")
        or (player == "2" and computer == "1")
        or (player == "3" and computer == "2")
    ):
        return "win"

    return "lose"


def play() -> None:
    """한 판(3판 2선승)을 진행한다. 끝나면 return 하여 메인 메뉴로 돌아간다."""
    import random

    player_wins = 0
    computer_wins = 0

    choices = ["1", "2", "3"]
    names = {
        "1": "가위",
        "2": "바위",
        "3": "보",
    }

    print(f"[{GAME_NAME}]")

    while player_wins < 2 and computer_wins < 2:
        player = input("1(가위) 2(바위) 3(보)를 선택하세요: ")

        if player not in choices:
            print("잘못된 입력입니다. 1, 2, 3 중에서 선택하세요.")
            continue

        computer = random.choice(choices)
        result = decide(player, computer)

        print(f"컴퓨터: {names[computer]}")

        if result == "win":
            player_wins += 1
            print("당신이 이겼습니다!")
        elif result == "lose":
            computer_wins += 1
            print("컴퓨터가 이겼습니다!")
        else:
            print("비겼습니다.")

        print(f"현재 점수: 나 {player_wins} - 컴퓨터 {computer_wins}")

    if player_wins == 2:
        print("게임에서 승리했습니다!")
    else:
        print("게임에서 패배했습니다!")
