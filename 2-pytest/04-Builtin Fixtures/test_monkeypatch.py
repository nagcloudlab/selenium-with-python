
import getpass

import pytest

class AuthenticationError(RuntimeError):
    pass


def check_credentials(name, password):
    if password == "wrong-pass":
        raise AuthenticationError("wrong password")
    return True

def user_login(name):
    password = getpass.getpass() # prompt for passwords
    check_credentials(name, password)
    ...
    return True

# --------------------------------------------------

def test_login_success(monkeypatch):
    monkeypatch.setattr(getpass, "getpass",lambda: "correct-pass")
    assert user_login("joe")


def test_login_failure(monkeypatch):
    monkeypatch.setattr(getpass, "getpass", lambda: "wrong-pass")
    with pytest.raises(AuthenticationError,match="wrong password"):
        user_login("joe")

# --------------------------------------------------


def get_os_user():
    import os
    return os.getenv("USER")

def test_get_od_user(monkeypatch):
    monkeypatch.setenv("USER", "testuser")
    assert get_os_user() == "testuser"


# --------------------------------------------------
# Replace the function with a mock
#----------------------------------------------------


# def send_email():
#     return "Email sent"

# def fake_send_email():
#     return "Fake email sent"

# def test_send_email(monkeypatch):
#     monkeypatch.setattr(__name__, "send_email", fake_send_email)
#     assert send_email() == "Fake email sent"