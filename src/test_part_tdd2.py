from src.part_tdd2 import zoek_anagram, zoek_palindroom


def test_zoek_palindroom_leeg(tmpdir):
    p = tmpdir.join("hello.txt")
    p.write("")

    result = zoek_palindroom(p)

    assert result == []


def test_zoek_palindroom_geen(tmpdir):
    p = tmpdir.join("hello.txt")
    p.write("banaan\nkip\nlap\nolifant")

    result = zoek_palindroom(p)

    assert result == []


def test_zoek_palindroom(tmpdir):
    p = tmpdir.join("hello.txt")
    p.write("lol\ntol\nevil\nmeetsysteem")
    result = zoek_palindroom(p)
    assert result == ["lol", "meetsysteem"]


def test_zoek_anagram_leeg(tmpdir):
    p = tmpdir.join("hello.txt")
    p.write("")

    result = zoek_anagram(p, "konijn")

    assert result == []


def test_zoek_anagram_geen(tmpdir):
    p = tmpdir.join("hello.txt")
    p.write("banaan\nkip\nlap\nolifant")

    result = zoek_anagram(p, "konijn")

    assert result == []


def test_zoek_anagram(tmpdir):
    p = tmpdir.join("hello.txt")
    p.write("lol\nkoelkast\aalscholver\nmeetsysteem\nkakstoel\n")
    result = zoek_anagram(p, "koelkast")
    assert result == ["kakstoel"]
