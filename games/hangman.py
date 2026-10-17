import random


"""행맨 — 담당:김민유 팀원 
"""

    행맨 — 담당:김민유 팀원
[규칙]
- 단어 목록에서 무작위로 하나를 고른다.
- 플레이어는 한 글자씩 추측하고, 틀리면 기회가 하나 줄어든다. (기회 6번)
- 맞힌 글자만 보여 준다.   예) a _ p l _

[구현 힌트] 테스트하기 쉽도록 순수 함수로 나눠 보세요.
- mask_word(word: str, guessed: set[str]) -> str
- is_solved(word: str, guessed: set[str]) -> bool
"""

GAME_NAME = "행맨"

# 게임에 사용할 단어 목록
WORDS = ["apple", "banana", "python", "hangman", "developer", "computer", "algorithm"]


def mask_word(word: str, guessed: set[str]) -> str:
    """단어에서 맞힌 글자는 그대로 보여 주고, 맞히지 못한 글자는 '_'로 가려진 문자열을 반환합니다."""
    return " ".join([char if char in guessed else "_" for char in word])


def is_solved(word: str, guessed: set[str]) -> bool:
    """단어의 모든 글자를 맞혔는지 여부를 반환합니다."""
    return all(char in guessed for char in word)


def play():

    """행맨 게임 메인 실행 함수"""
    word = random.choice(WORDS)
    guessed = set()
    attempts_left = 6

    print("=" * 40)
    print(" 🎮 행맨(Hangman) 게임에 오신 것을 환영합니다! ")
    print("=" * 40)

    while attempts_left > 0:
        print(f"\n남은 기회: {attempts_left}번")
        print(f"현재 단어: {mask_word(word, guessed)}")
        print(f"추측한 글자들: {', '.join(sorted(guessed)) if guessed else '없음'}")

        # 사용자 입력 받기
        guess = input("알파벳 한 글자를 입력하세요: ").lower().strip()

        # 입력값 검증
        if len(guess) != 1 or not guess.isalpha():
            print("❌ 알파벳 한 글자만 입력해 주세요.")
            continue

        if guess in guessed:
            print(f"⚠️ 이미 추측한 글자입니다: {guess}")
            continue

        guessed.add(guess)

        # 정답 여부 확인
        if guess in word:
            print(f"✨ 잘했습니다! '{guess}'는 단어에 포함되어 있습니다.")
        else:
            attempts_left -= 1
            print(f"❌ 틀렸습니다! '{guess}'는 단어에 없습니다.")

        # 게임 승리 조건 확인
        if is_solved(word, guessed):
            print("\n" + "=" * 40)
            print(f"🎉 축하합니다! 정답을 맞혔습니다. 정답은 '{word}'입니다!")
            print("=" * 40)
            return

    # 게임 패배 조건 확인
    print("\n" + "=" * 40)
    print(f"💀 기회를 모두 소진하여 패배했습니다. 정답은 '{word}'였습니다.")
    print("=" * 40)


if __name__ == "__main__":
    play()
