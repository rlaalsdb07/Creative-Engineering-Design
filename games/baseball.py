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

from utils import ask_int

GAME_NAME = "숫자 야구"
MAX_ATTEMPTS = 9


def make_answer() -> str:
    """서로 다른 숫자 3개로 이루어진 정답을 생성한다."""
    digits = random.sample("0123456789", 3)
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
        guess = ask_int(f"{attempt}번째 추측 (3자리 숫자): ", 100, 999)
        guess_str = str(guess)

        strike, ball = judge(answer, guess_str)

        if strike == 3:
            print(f"정답입니다! {attempt}번 만에 맞췄습니다. 정답: {answer}")
            return

        print(f"  → {strike} 스트라이크, {ball} 볼")

    print(f"기회를 모두 소진했습니다. 정답은 {answer}였습니다.")
