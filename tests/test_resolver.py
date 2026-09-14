import pytest

from netscope.resolver import resolve_target


def test_resolve_localhost():
    assert resolve_target("localhost") == "127.0.0.1"


def test_invalid_target():
    with pytest.raises(ValueError, match="Unable to resolve target"):
        resolve_target("this-host-does-not-exist.invalid")
