# 1D piškvorky s testy #

## Co to je? ##

Poté, co ses [naučila][defstr] pracovat s řetězci a psát vlastní funkce, dostala jsi za [úkol][handout4] naprogramovat si jednoduchou hru: jednorozměrné piškvorky. Zatím máš předepsané, z jakých dílčích funkcí se bude hra skládat. Toho využijeme a nahlédneme do pokročilejší lekce – té o [testování][testing].

[Testování][testing] ti pomůže ověřit, že tvůj program funguje, jak má. Neboj se však nic, všechno to složitější jsme zatím napsali za tebe. Ty tak můžeš postupovat podle [zadání][handout4] domácích projektů a testy ti spuštěním jednoho jednoduchého příkazu ukážou, jak moc blízko jsi dokončení programu.

**Pozor,** příkazy na této stránce jsou jen pro rychlou referenci a na svém počítači (zvláště máš-li Windows) možná budeš potřebovat trochu jiné. Podrobně je vše v [materiálech][course] ke kurzu, řiď se hlavně jimi. Odkaz na podřebnou stránku máš vždy u daného kroku.

## Jak na to? ##

1. Stáhni si tyto připravené soubory. Vpravo pod zeleným tlačítkem _Clone or download_ najdeš volbu _Download ZIP_.
2. Stažený archiv rozbal někam poblíž tvých stávajících projektů z PyLadies. Složku nech, tak jak je, jako celek, nepřesouvej z ní soubory pryč.
3. V příkazové řádce si složku otevři a vytvoř si v ní nové [virtuální prostředí][venvsetup]. To následně aktivuj.

```shell
$ python3 -m venv venv
$ . venv/bin/activate
(venv) $
```

4. Nainstaluj si knihovnu [pytest] podle [návodu][testing] v materiálech. Právě ta ti umožní ověřit správnou funkčnost programu.

```shell
(venv) $ pip install pytest
```

5. Opět podle [návodu][testing] [pytest] spusť.

```shell
(venv) $ pytest -v test_piskvorky.py
```

V souboru [_test_piskvorky.py_][testpiskvorky] máš připravené testy. Nic v něm neměň, ale můžeš se do něj podívat. Samotnou hru pak piš do připraveného souboru [_piskvorky.py_][piskvorky]. Máš tam nachystané všechny potřebné funkce, jen zatím nic nedělají. Až je všechny doplníš, budeš mít funkční hru.

## Co s tím? ##

[Pytest] ti vypíše, kde všude v tvém programu narazil na problém. Tyto jsou podrobně rozepsané a výstup je tak trochu dlouhý. Na jeho začátku však budeš mít takovéto řádky:

> test_piskvorky.py::test_vyhodnot_vyhra_x FAILED
> test_piskvorky.py::test_vyhodnot_vyhra_o FAILED
> test_piskvorky.py::test_vyhodnot_remiza FAILED
> …
> test_piskvorky.py::test_tah_pocitace_skoro_plne_konec_2 FAILED

Každé _FAILED_ znamená jednu chybu: jeden test, který neprošel. Protože jsi zatím nic nenapsala, je problém úplně ve všem. To se ale změní, jakmile splníš první úkol: zařídíš, aby funkce _vyhodnot_ rozpoznala, že vyhrál hráč s křížky.

> test_piskvorky.py::test_vyhodnot_vyhra_x PASSED
> test_piskvorky.py::test_vyhodnot_vyhra_o FAILED
> test_piskvorky.py::test_vyhodnot_remiza FAILED
> …
> test_piskvorky.py::test_tah_pocitace_skoro_plne_konec_2 FAILED

Vidíš? Výsledek prvního testu se změnil na _PASSED_. To znamená, že v tomto případě program funguje, jak má.

Až budeš mít program hotový, místo všech červených _FAILED_ bude u všech testů zelené _PASSED_. Pak víš, že máš hotovo. Teda, skoro.

> test_piskvorky.py::test_vyhodnot_vyhra_x PASSED
> test_piskvorky.py::test_vyhodnot_vyhra_o PASSED
> …
> test_piskvorky.py::test_tah_pocitace_skoro_plne_konec PASSED
> test_piskvorky.py::test_tah_pocitace_skoro_plne_konec_2 PASSED

Proč jen skoro? Některé věci testovat moc dobře nejdou, nebo by to bylo pro tebe v tuto chvíli moc složité.

* Jednou takovou věcí je zadání od uživatele. Funkci _tah_hrace_ proto [pytest] netestuje. To pak platí i pro celé jádro hry, funkci _piskvorky1d_, která právě funkci _tah_hrace_ používá, když je hráč na tahu.
* Druhou věcí, která není testy pokryta, je vypisování na obrazovku. Tedy všechna zvolání o chybách či stavu hry.

Tyto věci musíš ověřit ručně. To by ale nemuselo být tak hrozné: programuješ hru a testováním si rovnou i hraješ.

## Co dál? ##

Snad ti tato zkušenost ukázala, že automatické testování ti může ušetřit čas a práci. Že díky testům si můžeš být jistá, že jsi úpravou programu nerozbila nic, co před tím fungovalo.

Nahlédni do souboru [_test_piskvorky.py_][testpiskvorky]. Možná teď ještě nebudeš rozumět do detailu, jak to všechno vlastně funguje, ale i tak uvidíš, že to není raketová věda. Máš herní pole v nějakém stavu, zavoláš svou funkci, a ověříš, že vrátila to, co by měla.

```python
assert tah("--------------------", 10, 'x') == '----------x---------'
```

[Později][testing] se naučíš psát si testy sama. Snad ti tenhle malý exkurs ukázal, proč to není zbytečnost a že se ta trocha přidané námahy na začátku skutečně vyplatí.

## Kdo za to může? ##

* S nápadem přišel [@frenzymadness].
* Testy napsal [@encukou].
* Do kupy to dal, mustr a povídání napsal [@glutexo].

[defstr]: https://naucse.python.cz/2019/pyladies-ostrava-jaro/sessions/def-str/
[handout4]: http://pyladies.cz/v1/s004-strings/handout/handout4-ostrava.pdf
[course]: https://naucse.python.cz/2019/pyladies-ostrava-jaro/
[testing]: https://naucse.python.cz/2019/pyladies-ostrava-jaro/beginners/testing/
[venvsetup]: https://naucse.python.cz/2019/pyladies-ostrava-jaro/beginners/venv-setup/
[pytest]: https://pytest.readthedocs.io/
[testpiskvorky]: https://github.com/Glutexo/pyladies-piskvorky/blob/master/test_piskvorky.py
[piskvorky]: https://github.com/Glutexo/pyladies-piskvorky/blob/master/piskvorky.py
[@frenzymadness]: https://github.com/frenzymadness/
[@encukou]: https://github.com/encukou/
[@glutexo]: https://github.com/Glutexo/