"""숫자 야구 — 담당: 팀원 C 

[규칙]
- 컴퓨터가 서로 다른 숫자 3개를 정한다. (예: 3 7 1)
- 플레이어가 3자리를 추측하면 스트라이크(숫자·자리 모두 일치),
  볼(숫자만 일치)을 알려 준다. 최대 9번.

[구현 힌트]
- make_answer() -> str
- judge(answer: str, guess: str) -> tuple[int, int]   # (strike, ball)
"""

import random

GAME_NAME = "숫자 야구"
MAX_ATTEMPTS = 9


def make_answer() -> str:
    """서로 다른 숫자 3개로 이루어진 정답을 생성한다. (첫 자리는 0이 아님)"""
    first = random.choice("123456789")
    remaining = [d for d in "0123456789" if d != first]
    digits = [first] + random.sample(remaining, 2)
    return "".join(digits)


def judge(answer: str, guess: str) -> tuple[int, int]:
    """정답과 추측을 비교해 (스트라이크, 볼)을 반환한다."""
    strike = sum(a == g for a, g in zip(answer, guess))
    ball = sum(g in answer for g in guess) - strike
    return strike, ball


def play() -> None:
    """한 판을 진행한다. 끝나면 return 하여 메인 메뉴로 돌아간다."""
    answer = make_answer()
    print(f"[{GAME_NAME}] 게임을 시작합니다! (기회: {MAX_ATTEMPTS}번)")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        while True:
            guess = input(f"{attempt}번째 추측 (3자리 숫자): ").strip()
            if len(guess) == 3 and guess.isdigit() and guess[0] != "0":
                break
            print("3자리 숫자를 입력하세요. (첫 자리는 0이 될 수 없습니다.)")

        strike, ball = judge(answer, guess)

        if strike == 3:
            print(f"정답입니다! {attempt}번 만에 맞췄습니다. 정답: {answer}")
            return

        print(f"  → {strike} 스트라이크, {ball} 볼")

    print(f"기회를 모두 소진했습니다. 정답은 {answer}였습니다.")
