#!/usr/bin/env python

from random import randrange


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
    while True:
        vstup_uzivatele = input("Na jaké políčko chceš hrát? ")

        if not vstup_uzivatele.isdigit():
            print("Neplatné číslo políčka")
            continue

        cislo_policka = int(vstup_uzivatele)

        if cislo_policka < 0 or cislo_policka > len(pole) - 1:
            print("Tah mimo herní pole")
            continue

        if pole[cislo_policka] != "-":
            print("Tah na obsazené pole")
            continue

        try:
            return tah(pole, cislo_policka, SYMBOL_HRACE)
        except (IndexError, ValueError) as exception:  # Chybné zadání
            print(exception)
            continue


def tah_pocitace(pole):
    """
    Vrátí herní pole se zaznamenaným tahem počítače
    """
    while True:
        cislo_policka = randrange(len(pole))
        if pole[cislo_policka] != "-":  # Obsazené pole
            continue
        return tah(pole, cislo_policka, SYMBOL_POCITACE)


def piskvorky1d():
    """
    Hraje 1D piškvorky.
    """
    pole = "-" * DELKA_POLE
    while True:
        print(pole)
        stav = vyhodnot(pole)
        if stav == "-":
            pole = tah_hrace(pole)
            pole = tah_pocitace(pole)
            continue
        elif stav == "!":
            print("Remíza")
            break
        elif stav == "x":
            print("Vyhrála jsi")
            break
        elif stav == "o":
            print("Vyhrál počítač")
            break
        else:
            print("Jsem v koncích")  # Neznámý stav hry
            break


if __name__ == "__main__":
    piskvorky1d()
