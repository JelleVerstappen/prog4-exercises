import random

import pytest

random.seed(100)

from .t2_wordle import (
    choose_word,
    combine_letters_of_words,
    lines_to_words,
    print_letter,
    print_letter_bijna_juist,
    print_letter_fout,
    print_letter_volledig_juist,
    process_words,
)


def test_choose_word():
    words = [
        "kip",
        "aap",
        "konijn",
    ]
    word = choose_word(words)
    assert word == "kip"


def test_process_words_3():
    words = [
        "kip",
        "aap",
        "konijn",
        "karma",
        "rookt",
    ]
    result = process_words(words, 3)
    expected = ["kip", "aap"]
    assert result == expected


def test_process_words_5():
    words = [
        "kip",
        "aap",
        "konijn",
        "karma",
        "rookt",
    ]
    result = process_words(words, 5)
    expected = ["karma", "rookt"]
    assert result == expected


def test_process_words_dash():
    words = [
        "mus",
        "aap",
        "D-Day",
        "3-tal",
    ]
    result = process_words(words, 3)
    expected = ["mus", "aap"]
    assert result == expected


def test_process_words_dots():
    words = [
        "mis",
        "aap",
        "mevr.",
    ]
    result = process_words(words, 3)
    expected = ["mis", "aap"]
    assert result == expected


def test_process_words_quote():
    words = [
        "kip",
        "rap",
        "soa's",
    ]
    result = process_words(words, 3)
    expected = ["kip", "rap"]
    assert result == expected


def test_process_words_space():
    words = [
        "lip",
        "aap",
        "WO II",
    ]
    result = process_words(words, 3)
    expected = ["lip", "aap"]
    assert result == expected


def test_process_words_caps():
    words = [
        "lip",
        "aap",
        "Bruno",
    ]
    result = process_words(words, 3)
    expected = ["lip", "aap"]
    assert result == expected


def test_process_words():
    words = [
        "kip",
        "aap",
        "konijn",
        "karma",
        "rookt",
        "D-Day",
        "3-tal",
        "mevr.",
        "soa's",
        "WO II",
        "Bruno",
        "ASCII",
    ]
    result = process_words(words, 5)
    expected = ["karma", "rookt"]
    assert result == expected


def test_lines_to_words():
    lines = [
        "kip\n",
        "aap\n\r",
        "karma\r\n",
        "rookt",
    ]
    words = lines_to_words(lines)
    expected = [
        "kip",
        "aap",
        "karma",
        "rookt",
    ]
    assert words == expected


def test_combine_letters_of_words_abcd():
    word1 = "ab"
    word2 = "cd"
    result = combine_letters_of_words(word1, word2)
    expected = [("a", "c"), ("b", "d")]
    assert list(result) == expected


def test_combine_letters_of_words():
    word1 = "kip"
    word2 = "aap"
    result = combine_letters_of_words(word1, word2)
    expected = [("k", "a"), ("i", "a"), ("p", "p")]
    assert list(result) == expected


def test_print_letter_volledig_juist():
    result = print_letter_volledig_juist("g")
    assert result == "[green]g[/green]"


def test_print_letter_bijna_juist():
    result = print_letter_bijna_juist("f")
    assert result == "[yellow]f[/yellow]"


def test_print_letter_fout():
    result = print_letter_fout("e")
    assert result == "[red]e[/red]"


def test_print_letter_1():
    result = print_letter("i", "i", "kip")
    assert result == "[green]i[/green]"


def test_print_letter_2():
    result = print_letter("i", "k", "kip")
    assert result == "[yellow]i[/yellow]"


def test_print_letter_3():
    result = print_letter("e", "k", "kip")
    assert result == "[red]e[/red]"
