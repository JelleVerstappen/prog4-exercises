from src.part_tdd import anagram, leeftijd, palindroom


def test_palindroom_lol():
    assert palindroom("lol") is True


def test_palindroom_tol():
    assert palindroom("tol") is False


def test_palindroom_meetsysteem():
    assert palindroom("meetsysteem") is True


def test_palindroom_stormrots():
    assert palindroom("stormrots") is True


def test_palindroom_stormrot():
    assert palindroom("stormrot") is False


def test_anagram_tol_lot():
    assert anagram("tol", "lot") is True


def test_anagram_tol_lol():
    assert anagram("tol", "lol") is False


def test_anagram_omicron():
    assert anagram("omicron", "moronic") is True


def test_anagram_evil():
    assert anagram("evil", "vile") is True


def test_anagram_koelkast():
    assert anagram("kakstoel", "koelkast") is True


def test_anagram_new_york_times():
    assert anagram("New York Times", "monkeys write") is True


def test_anagram_new_york_times_false():
    assert anagram("New York Times", "monkey write") is False


def test_anagram_cos():
    assert anagram("Church of Scientology", "rich-chosen goofy cult") is True


def test_anagram_cos_false():
    assert anagram("Church of Scientology", "rich-choosen goofy cult") is False


def test_anagram_mdr():
    assert anagram("McDonald's restaurants", "Uncle Sam's standard rot") is True


def test_anagram_mdr_false():
    assert anagram("McDonald's restaurant", "Uncle Sam's standard rot") is False


def test_anagram_shakespeare():
    assert anagram("William Shakespeare", "I am a weakish speller") is True


def test_anagram_shakespeare_false():
    assert anagram("William Shakespeare", "I am a weakish speler") is False


def test_anagram_voldemort():
    assert anagram("Tom Marvolo Riddle", "I am Lord Voldemort") is True


def test_leeftijd_44():
    assert leeftijd(1976, 12, 20) == 44


def test_leeftijd_45():
    assert leeftijd(1976, 11, 22) == 45


def test_leeftijd_14():
    assert leeftijd(2007, 8, 6) == 14


def test_leeftijd_10():
    assert leeftijd(2011, 9, 21) == 10


def test_leeftijd_7():
    assert leeftijd(2014, 3, 4) == 7


def test_leeftijd_74():
    assert leeftijd(1947, 11, 11) == 74


def test_leeftijd_75():
    assert leeftijd(1946, 2, 21) == 75


def test_leeftijd_51():
    assert leeftijd(1970, 8, 22) == 51
