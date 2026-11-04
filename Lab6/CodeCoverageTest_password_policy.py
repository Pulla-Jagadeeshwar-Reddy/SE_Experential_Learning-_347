"""Code (line) coverage tests for password_policy.py"""
import pytest
from password_policy import check_password, strength, suggest_fix


# ---------- check_password ----------
def test_valid_password_has_no_issues():
    assert check_password("Abcdef1!") == []


def test_too_short():
    assert "too short" in check_password("Ab1!")


def test_too_long():
    assert "too long" in check_password("Aa1!" + "a" * 61)  # 65 chars


def test_common_password():
    assert "common" in check_password("password")


def test_common_password_case_insensitive():
    assert "common" in check_password("PASSWORD")


def test_no_uppercase():
    assert check_password("abcdef1!") == ["no uppercase"]


def test_no_lowercase():
    assert check_password("ABCDEF1!") == ["no lowercase"]


def test_no_digit():
    assert check_password("Abcdefg!") == ["no digit"]


def test_no_special():
    assert check_password("Abcdefg1") == ["no special"]


# ---------- strength ----------
def test_valid_password_is_good():
    assert strength("Abcdef1!") == "good"


def test_strong_password():
    assert strength("Abcdefghijkl1!") == "strong"


def test_weak_password():
    assert strength("abcdef1!") == "weak"


def test_very_weak_password():
    assert strength("abc") == "very weak"


# ---------- suggest_fix ----------
def test_suggest_fix_none_needed():
    assert suggest_fix([]) == "none needed"


def test_suggest_fix_too_short():
    assert suggest_fix(["too short"]) == "add more characters"


def test_suggest_fix_common():
    assert suggest_fix(["common"]) == "avoid common passwords"


def test_suggest_fix_missing_class():
    assert suggest_fix(["no digit"]) == "add digit"


def test_suggest_fix_too_long():
    assert suggest_fix(["too long"]) == "shorten it"
