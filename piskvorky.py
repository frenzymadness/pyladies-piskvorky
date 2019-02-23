#!/usr/bin/env python

DELKA_POLE = 20

SYMBOL_HRACE = "x"
SYMBOL_POCITACE = "o"

POTREBA_K_VYHRE = 3


def vyhodnot(pole):
    """
    Vrátí x (výhra x), o (výhra o), ! (remíza), - (hra neskončila) podle stavu
    hry.
    """
    if SYMBOL_HRACE * POTREBA_K_VYHRE in pole:
        return "x"
    elif SYMBOL_POCITACE * POTREBA_K_VYHRE in pole:
        return "o"
    elif "-" in pole:
        return "-"
    else:
        return "!"


def tah(pole: object, cislo_policka: object, symbol: object) -> object:
    """
    Vrátí herní pole s daným symbolem umístěným na danou pozici.
    """
    pred = pole[0:cislo_policka]
    po = pole[cislo_policka+1:]
    return pred + symbol + po


def tah_hrace(pole):
    """
    Zeptá se hráče, kam chce hrát, a vrátí herní pole s jeho zaznamenaným
    tahem.
    """
    pass


def tah_pocitace(pole):
    """
    Vrátí herní pole se zaznamenaným tahem počítače
    """
    pass


def piskvorky1d():
    """
    Hraje 1D piškvorky.
    """
    pass


if __name__ == "__main__":
    piskvorky1d()
