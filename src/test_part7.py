from .part7 import *


def test_write_rick_and_morty(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "ram.txt"

    write_rick_and_morty(p)

    with open(p, "rt") as f:
        line = f.read()
        assert line == "Rick and Morty"


def test_write_numbers_0_100(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "nummers.txt"

    write_numbers(p)

    with open(p, "rt") as f:
        lines = f.readlines()
        assert len(lines) == 100
        expected = [f"{i}\n" for i in range(100)]
        assert lines == expected


def test_write_numbers_and_squares_0_100(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "nummers.txt"

    write_numbers_and_squares(p)

    with open(p, "rt") as f:
        lines = f.readlines()
        assert len(lines) == 100
        expected = [f"{i},{i**2}\n" for i in range(100)]
        assert lines == expected


def test_sum_numbers_from_file_empty(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "nummers.txt"
    with open(p, "wt") as f:
        f.write("")

    result = sum_numbers_from_file(p)

    assert result == 0


def test_sum_numbers_from_file_one(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "nummers.txt"
    with open(p, "wt") as f:
        f.write("42\n")

    result = sum_numbers_from_file(p)

    assert result == 42


def test_sum_numbers_from_file_many_numbers(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "nummers.txt"
    with open(p, "wt") as f:
        f.write("4900\n")
        f.write("90\n")
        f.write("6\n")
        f.write("3\n")
        f.write("1\n")

    result = sum_numbers_from_file(p)

    assert result == 5000


def test_sum_numbers_from_file_empty_lines(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "nummers.txt"
    with open(p, "wt") as f:
        f.write("\n")
        f.write("\n")
        f.write("\n")
        f.write("\n")

    result = sum_numbers_from_file(p)

    assert result == 0


def test_sum_two_columns_of_numbers_from_file_one(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "nummers.txt"
    with open(p, "wt") as f:
        f.write("42,4096\n")

    result = sum_two_columns_of_numbers_from_file(p)

    assert result == (42, 4096)


def test_sum_two_columns_of_numbers_from_file_five(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "nummers.txt"
    with open(p, "wt") as f:
        f.write("4900,10\n")
        f.write("90,5\n")
        f.write("6,9\n")
        f.write("3,1000\n")
        f.write("1,0\n")

    result = sum_two_columns_of_numbers_from_file(p)

    assert result == (5000, 1024)


def test_count_words_from_file_one_line(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "tekst.txt"
    with open(p, "wt") as f:
        f.write("Okay, you know what, Rick? You are acting weird, too.")
    result = count_words_from_file(p)

    assert result == 10


def test_count_words_from_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "tekst.txt"
    with open(p, "wt") as f:
        f.write(
            """It was still gruesomely dark when, not much over an hour later, a
confused babel of voices sounded down the road. Another moment brought
to view a frightened group of more than a dozen men, running, shouting,
and even whimpering hysterically. Someone in the lead began sobbing out
words, and the Arkham men started violently when those words developed
a coherent form."""
        )
    result = count_words_from_file(p)

    assert result == 62


def test_count_word_frequency_from_file_one_line(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "tekst.txt"
    with open(p, "wt") as f:
        f.write("Okay, you know what, Rick? You are acting weird, too.")
    result = count_word_frequency_from_file(p)

    expected = {
        "acting": 1,
        "are": 1,
        "know": 1,
        "okay": 1,
        "rick": 1,
        "too": 1,
        "weird": 1,
        "what": 1,
        "you": 2,
    }
    assert result == expected


def test_count_word_frequency_from_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "tekst.txt"
    with open(p, "wt") as f:
        f.write(
            """It was still gruesomely dark when, not much over an hour later, a
confused babel of voices sounded down the road. Another moment brought
to view a frightened group of more than a dozen men, running, shouting,
and even whimpering hysterically. Someone in the lead began sobbing out
words, and the Arkham men started violently when those words developed
a coherent form."""
        )
    result = count_word_frequency_from_file(p)

    expected = {
        "a": 4,
        "an": 1,
        "and": 2,
        "another": 1,
        "arkham": 1,
        "babel": 1,
        "began": 1,
        "brought": 1,
        "coherent": 1,
        "confused": 1,
        "dark": 1,
        "developed": 1,
        "down": 1,
        "dozen": 1,
        "even": 1,
        "form": 1,
        "frightened": 1,
        "group": 1,
        "gruesomely": 1,
        "hour": 1,
        "hysterically": 1,
        "in": 1,
        "it": 1,
        "later": 1,
        "lead": 1,
        "men": 2,
        "moment": 1,
        "more": 1,
        "much": 1,
        "not": 1,
        "of": 2,
        "out": 1,
        "over": 1,
        "road": 1,
        "running": 1,
        "shouting": 1,
        "sobbing": 1,
        "someone": 1,
        "sounded": 1,
        "started": 1,
        "still": 1,
        "than": 1,
        "the": 3,
        "those": 1,
        "to": 1,
        "view": 1,
        "violently": 1,
        "voices": 1,
        "was": 1,
        "when": 2,
        "whimpering": 1,
        "words": 2,
    }
    assert result == expected
