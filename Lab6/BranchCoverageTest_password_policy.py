"""Branch coverage tests for password_policy.py
Every decision is exercised both True and False, including loop entry/exit.
"""
import pytest
from password_policy import check_password, strength, suggest_fix


# ---------- check_password: length branches ----------
def test_valid_password_has_no_issues():
    assert check_password("Abcdef1!") == []


def test_too_short():  # len < 8 True
    assert check_password("Ab1!") == ["too short"]


def test_length_boundary_8_ok():  # len == 8 -> not short
    assert "too short" not in check_password("Abcdef1!")


def test_length_boundary_7_short():
    assert "too short" in check_password("Abcde1!")


def test_length_boundary_64_ok():  # len == 64 -> not long (elif False)
    pw = "Aa1!" + "a" * 60
    assert len(pw) == 64
    assert check_password(pw) == []


def test_length_boundary_65_long():  # elif True
    pw = "Aa1!" + "a" * 61
    assert len(pw) == 65
    assert check_password(pw) == ["too long"]


# ---------- check_password: common branch ----------
def test_common_true():
    assert check_password("password")[0] == "common"


def test_common_true_mixed_case():
    assert "common" in check_password("PaSsWoRd")


def test_common_false():
    assert "common" not in check_password("Abcdef1!")


# ---------- check_password: character loop branches ----------
def test_empty_password_loop_not_entered():
    assert check_password("") == [
        "too short", "no uppercase", "no lowercase", "no digit", "no special"
    ]


def test_all_character_classes_present():
    assert check_password("Aa1!Aa1!") == []


def test_no_uppercase():
    assert check_password("abcdef1!") == ["no uppercase"]


def test_no_lowercase():
    assert check_password("ABCDEF1!") == ["no lowercase"]


def test_no_digit():
    assert check_password("Abcdefg!") == ["no digit"]


def test_no_special():
    assert check_password("Abcdefg1") == ["no special"]


# ---------- strength: all three decisions, both ways ----------
def test_strength_good():  # no issues, len < 14
    assert strength("Abcdef1!") == "good"


def test_strength_strong_boundary_14():  # len >= 14 True
    pw = "Abcdefghijk1!a"
    assert len(pw) == 14
    assert strength(pw) == "strong"


def test_strength_good_boundary_13():  # len >= 14 False
    pw = "Abcdefghijk1!"
    assert len(pw) == 13
    assert strength(pw) == "good"


def test_strength_weak_one_issue():  # len(issues) <= 2 True
    assert strength("abcdef1!") == "weak"


def test_strength_weak_two_issues():  # boundary == 2
    assert check_password("abcdefgh!") == ["no uppercase", "no digit"]
    assert strength("abcdefgh!") == "weak"


def test_strength_very_weak():  # len(issues) <= 2 False
    assert strength("abc") == "very weak"


# ---------- suggest_fix: each branch ----------
def test_suggest_fix_no_issues():
    assert suggest_fix([]) == "none needed"


def test_suggest_fix_too_short():
    assert suggest_fix(["too short"]) == "add more characters"


def test_suggest_fix_common():
    assert suggest_fix(["common"]) == "avoid common passwords"


@pytest.mark.parametrize("issue,expected", [
    ("no uppercase", "add uppercase"),
    ("no lowercase", "add lowercase"),
    ("no digit", "add digit"),
    ("no special", "add special"),
])
def test_suggest_fix_missing_class(issue, expected):
    assert suggest_fix([issue]) == expected


def test_suggest_fix_default_shorten():  # falls through every if
    assert suggest_fix(["too long"]) == "shorten it"


def test_suggest_fix_uses_only_first_issue():
    assert suggest_fix(["too short", "no digit"]) == "add more characters"


def test_suggest_fix_end_to_end():
    assert suggest_fix(check_password("password")) == "avoid common passwords"
