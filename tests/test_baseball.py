"""숫자 야구 테스트"""

import games.baseball as baseball


def test_make_answer_unique_digits():
    """정답은 중복 없는 3자리 숫자여야 한다."""
    for _ in range(100):
        ans = baseball.make_answer()
        assert len(ans) == 3
        assert len(set(ans)) == 3
        assert ans.isdigit()


def test_judge_all_strike():
    """숫자와 자리가 모두 맞으면 3 스트라이크, 0 볼."""
    assert baseball.judge("123", "123") == (3, 0)


def test_judge_all_ball():
    """숫자는 맞지만 자리가 모두 다르면 0 스트라이크, 3 볼."""
    assert baseball.judge("123", "312") == (0, 3)


def test_judge_mixed():
    """일부는 스트라이크, 일부는 볼인 경우."""
    assert baseball.judge("123", "132") == (1, 2)  # 1은 자리도 같음, 2,3은 자리 다름
    assert baseball.judge("123", "456") == (0, 0)  # 모두 틀림
    assert baseball.judge("123", "145") == (1, 0)  # 1만 맞음


def test_judge_edge_cases():
    """0이 포함된 경우도 정상 동작해야 한다."""
    assert baseball.judge("012", "012") == (3, 0)
    assert baseball.judge("012", "210") == (1, 2)
