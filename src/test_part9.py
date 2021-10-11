from unittest.mock import mock_open, patch

from .part9 import *


def test_book_title():
    b = Book(title="GIP")

    assert b.content == "Title: GIP\n"
def test_book_chapter():
    b = Book(title="GIP")
    b.add_chapter("Introductie")

    expected = """Title: GIP
# Introductie
"""
    assert b.content == expected


def test_book_chapters():
    b = Book(title="GIP")
    b.add_chapter("Introductie")
    b.add_chapter("Werkwijze")
    b.add_chapter("Conclusie")

    expected = """Title: GIP
# Introductie
# Werkwijze
# Conclusie
"""
    assert b.content == expected


def test_book_contents():
    b = Book(title="GIP")
    b.add_line("Dit is de introductie")

    expected = """Title: GIP
Dit is de introductie
"""
    assert b.content == expected


def test_book_contents_2_lines():
    b = Book(title="GIP")
    b.add_line("Dit is regel 1")
    b.add_line("Dit is regel 2")

    expected = """Title: GIP
Dit is regel 1
Dit is regel 2
"""
    assert b.content == expected


def test_book_complete():
    b = Book(title="GIP")
    b.add_chapter("Introductie")
    b.add_line("Dit is de introductie")
    b.add_chapter("Werkwijze")
    b.add_line("We bestudeerden eerst het probleem door ...")
    b.add_chapter("Conclusie")
    b.add_line("Bij aanvang van deze GIP, ...")

    expected = """Title: GIP
# Introductie
Dit is de introductie
# Werkwijze
We bestudeerden eerst het probleem door ...
# Conclusie
Bij aanvang van deze GIP, ...
"""
    assert b.content == expected


def test_book_write_title():

    m = mock_open()
    with patch("builtins.open", m):
        b = Book(title="GIP")
        b.write("uitvoer.md")

        m.assert_called_once_with("uitvoer.md", "wt")
        handle = m()

        expected = "Title: GIP\n"
        handle.write.assert_called_with(expected)


def test_book_write():
    m = mock_open()
    with patch("builtins.open", m):
        b = Book(title="GIP")
        b.add_line("Dit is de inhoud")
        b.write("uitvoer.md")

        m.assert_called_once_with("uitvoer.md", "wt")
        handle = m()

        expected = """Title: GIP
Dit is de inhoud
"""
        handle.write.assert_called_with(expected)