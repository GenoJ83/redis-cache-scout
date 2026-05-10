from src.rules.naming import check_naming_convention

def test_naming_rules():
    assert check_naming_convention("user:123:profile") is True
    assert check_naming_convention("user 123 profile!!") is False
