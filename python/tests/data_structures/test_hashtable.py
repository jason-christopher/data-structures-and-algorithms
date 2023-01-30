import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_get_silent():
    hashtable = Hashtable()
    hashtable.set("ahmad", 30)
    hashtable.set("silent", "yes")
    hashtable.set("listen", "to me")
    actual = hashtable.get("silent")
    expected = "yes"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_has_listen():
    hashtable = Hashtable()
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    actual = hashtable.has("listen")
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_has_not_in_table():
    hashtable = Hashtable()
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    actual = hashtable.has("jason")
    expected = False
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_keys_3():
    hashtable = Hashtable()
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    actual = sorted(hashtable.keys())
    expected = sorted(["ahmad", "silent", "listen"])
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_keys_empty():
    hashtable = Hashtable()
    actual = hashtable.keys()
    expected = []
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_hash_silent():
    hashtable = Hashtable()
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    actual = hashtable._hash("silent")
    expected = hash("silent") % 10
    assert actual == expected
