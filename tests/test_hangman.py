"""행맨 게임 순수 함수 테스트 코드"""

from games import hangman

def test_mask_word():
    """mask_word 함수가 맞힌 글자는 보여 주고 나머지는 '_'로 가려 주는지 테스트합니다."""
    word = "python"
    
    # 아무것도 맞히지 않은 경우
    assert hangman.mask_word(word, set()) == "_ _ _ _ _ _"
    
    # 일부 글자를 맞힌 경우
    assert hangman.mask_word(word, {"p", "t"}) == "p _ _ t _ _"
    
    # 모든 글자를 맞힌 경우
    assert hangman.mask_word(word, {"p", "y", "t", "h", "o", "n"}) == "p y t h o n"

def test_is_solved():
    """is_solved 함수가 단어의 모든 글자를 맞혔는지 여부를 정확히 판단하는지 테스트합니다."""
    word = "python"
    
    # 맞히다 만 경우
    assert hangman.is_solved(word, {"p", "y"}) is False
    
    # 모든 글자를 다 맞힌 경우
    assert hangman.is_solved(word, {"p", "y", "t", "h", "o", "n"}) is True
    
    # 단어에 없는 글자가 포함되어 있어도 구성 글자를 다 맞혔다면 True
    assert hangman.is_solved(word, {"p", "y", "t", "h", "o", "n", "a", "b"}) is True