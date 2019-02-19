from piskvorky import tah, tah_pocitace, vyhodnot
import pytest


def test_vyhodnot_vyhra_x():
    """
    Křížky vyhrály.
    """
    assert vyhodnot("xxx-----------------") == 'x'


def test_vyhodnot_vyhra_o():
    """
    Kolečka vyhrála.
    """
    assert vyhodnot("ooo-----------------") == 'o'


def test_vyhodnot_remiza():
    """
    Nastala remíza.
    """
    assert vyhodnot("oxoxoxoxoxoxoxoxoxox") == '!'
    assert vyhodnot("xxooxxooxxooxxooxxoo") == '!'


def test_vyhodnot_hra():
    """
    Hra neskončila.
    """
    assert vyhodnot("xx----------------oo") == '-'
    assert vyhodnot("-xoxoxoxoxoxoxoxoxox") == '-'
    assert vyhodnot("-xooxxooxxooxxooxxoo") == '-'
    assert vyhodnot("xoxoxoxoxoxoxoxoxox-") == '-'
    assert vyhodnot("xooxxooxxooxxooxxoo-") == '-'
    assert vyhodnot("oxoxoxoxo-oxoxoxoxox") == '-'
    assert vyhodnot("xxooxxoox-ooxxooxxoo") == '-'


def test_tah_x():
    """
    Pozitivní testy se symbolem "x".
    """
    assert tah("--------------------", 0, 'x') == 'x-------------------'
    assert tah("--------------------", 10, 'x') == '----------x---------'
    assert tah("--------------------", 19, 'x') == '-------------------x'


def test_tah_o():
    """
    Pozitivní testy se symbolem "o".
    """
    assert tah("--------------------", 0, 'o') == 'o-------------------'
    assert tah("--------------------", 10, 'o') == '----------o---------'
    assert tah("--------------------", 19, 'o') == '-------------------o'


def test_tah_obsazeno():
    """
    Hra na obsazené políčko by měla skončit chybou IndexError.
    """
    with pytest.raises(IndexError):
        tah("o-------------------", 0, "o")
    with pytest.raises(IndexError):
        tah("----------x---------", 10, "o")


def test_tah_index404():
    """
    Hra na pozici, co není v poli, by měla skončit chybou IndexError.
    """
    with pytest.raises(IndexError):
        tah("--------------------", 20, "x")


def test_tah_minus1():
    """
    Hra na zápornou pozici by měla skončit chybou IndexError.
    """
    with pytest.raises(IndexError):
        tah("--------------------", -1, "x")


def test_tah_spatny_symbol():
    """
    Hra jiným symbolem než \"o\" a \"x\" by měla skončit chybou ValueError.
    """
    with pytest.raises(ValueError):
        tah("--------------------", 2, "m")


def test_tah_spatny_symbol_ox():
    """
    Hra více symboly by měla skončit chybou ValueError.
    """
    with pytest.raises(ValueError):
        tah("--------------------", 2, "xo")
    with pytest.raises(ValueError):
        tah("--------------------", 2, "ox")


def test_tah_10():
    """
    Pozitivní testy s délkou pole 10.
    """
    assert tah("----------", 0, 'x') == "x---------"
    assert tah("----------", 9, 'x') == "---------x"
    assert tah("----------", 0, 'o') == "o---------"
    assert tah("----------", 9, 'o') == "---------o"


def test_tah_30():
    """
    Pozitivní testy s délkou pole 30.
    """
    assert tah("-" * 30, 0, 'x') == "x" + "-" * 29
    assert tah("-" * 30, 29, 'x') == "-" * 29 + "x"
    assert tah("-" * 30, 0, 'o') == "o" + "-" * 29
    assert tah("-" * 30, 29, 'o') == "-" * 29 + "o"


def test_indexmax_10():
    """
    Hra na pozici, co není v poli, by měla skončit chybou IndexError.
    """
    with pytest.raises(IndexError):
        tah("-" * 10, 10, "x")
    with pytest.raises(IndexError):
        tah("-" * 30, 30, "o")
    with pytest.raises(IndexError):
        tah("", 0, "x")


def test_tah_pocitace_prazdne():
    """
    Hra na prázdné pole.
    """
    result = tah_pocitace("-" * 20)
    assert len(result) == 20
    assert result.count("-") == 19
    assert result.count("o") == 1


def test_tah_pocitace_skoro_plne():
    """
    Hra na skoro plné pole (volno uprostřed).
    """
    pole = "xoxoxoxoxo-xoxoxoxox"
    result = tah_pocitace(pole)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10


def test_tah_pocitace_skoro_plne_zacatek():
    """
    Hra na skoro plné pole (volno na začátku).
    """
    pole = "-xoxoxoxoxoxoxoxoxox"
    result = tah_pocitace(pole)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10


def test_tah_pocitace_skoro_plne_konec():
    """
    Hra na skoro plné pole (volno na konci).
    """
    pole = "xoxoxoxoxoxoxoxoxox-"
    result = tah_pocitace(pole)
    assert len(result) == 20
    assert result.count("x") == 10
    assert result.count("o") == 10


def test_tah_pocitace_skoro_plne_konec_2():
    """
    Hra na skoro plné pole (2× volno na konci).
    """
    pole = "xooxxooxoxoxoxooxx--"
    result = tah_pocitace(pole)
    assert len(result) == 20
    assert result.count("x") == 9
    assert result.count("o") == 10


def test_tah_pocitace_kratke():
    """
    Hra počítače na krátké pole.
    """
    result = tah_pocitace("-" * 5)
    assert len(result) == 5
    assert result.count("-") == 4
    assert result.count("o") == 1


def test_tah_pocitace_dlouhe():
    """
    Hra počítače na dlouhé pole.
    """
    result = tah_pocitace("-" * 100)
    assert len(result) == 100
    assert result.count("-") == 99
    assert result.count("o") == 1


def test_tah_pocitace_nulove():
    """
    Hra počítače na pole nulové délky.
    """
    with pytest.raises(ValueError):
        tah_pocitace("")


def test_tah_pocitace_plne():
    """
    Hra počítače na plné pole.
    """
    with pytest.raises(ValueError):
        tah_pocitace("xo" * 10)
