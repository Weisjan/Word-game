# Gra słowna

Implementacja popularnej gry słownej "Wordle" przy użyciu frameworku Flask. Gracze mają sześć prób na odgadnięcie losowo wybranego 5-literowego słowa. Po każdej próbie, gracz otrzymuje kolorowe podpowiedzi wskazujące, czy litery w słowie są poprawne i na właściwej pozycji (zielony), poprawne, ale na niewłaściwej pozycji (żółty), czy niepoprawne (czerwony).

## Wymagania

* Python 3.10
* Flask 3.0.3

## Struktura Plików

```
Words-game
├── templates
│   ├── index.html
│   ├── lose.html
│   └──  win.html
├── wordle.py
├── words_eng.txt
└── Readme.md
```

| No | File Name | Details 
|----|------------|-------|
| 1  | wordle.py | Główny plik aplikacji zawierający trasy Flask i logikę gry
| 2 | index.html | Główny szablon HTML dla interfejsu gry
| 3  | win.html | Szablon HTML wyświetlany, gdy gracz wygra
| 4 | lose.html | Szablon HTML wyświetlany, gdy gracz przegra
| 5 | words_eng.txt | Plik tekstowy zawierający listę 5-literowych słów
| 6 | Readme.md | Plik Readme

## Instalacja

1. Sklonuj repozytorium:
    ```
    git clone https://github.com/Weisjan/Words-game.git
    ```

2. Uruchom plik `wordle.py`

3. Otwórz przeglądarkę internetową i przejdź do `http://127.0.0.1:5000/`, aby rozpocząć grę.

## Opis Działania

#### Gra (`worlde.py`)

Ten plik zawiera główny kod aplikacji. Kluczowe części pliku to:

- **Importy i Konfiguracja**: Ustawienia Flask i importy niezbędnych modułów.
- **Trasy**:
  - `/`: Główna trasa obsługująca logikę gry i renderowanie głównej strony gry.
  - `/gameover`: Trasa obsługująca zakończenie gry, gdy gracz wygra.
  - `/gameover_lose`: Trasa obsługująca zakończenie gry, gdy gracz przegra.
- **Logika Gry**:
  - Inicjalizuje nową grę z losowym słowem z pliku `words_eng.txt`.
  - Obsługuje zgadywanie przez gracza, dostarczając informacje zwrotne i śledząc pozostałe próby.
  - Przekierowuje na odpowiednie strony zakończenia gry w zależności od wyniku.

#### Index (`index.html`)

Główny interfejs gry. Zawiera:

- Formularz do wpisywania słów.
- Wyświetlanie pozostałych prób.
- Wyświetlanie poprzednich słów z kolorowymi podpowiedziami.

#### Wygrana (`win.html`)

Wyświetlany, gdy gracz poprawnie zgadnie słowo.

#### Przegrana (`lose.html`)

Wyświetlany, gdy gracz wyczerpie wszystkie próby nie zgadując słowa.

## Uwagi

- **Lista Słów**: Możesz zaktualizować plik `words_eng.txt`, aby zawierał własną listę 5-literowych słów.
- **Stylizacja**: Dostosuj style CSS w plikach HTML, aby zmienić wygląd gry.

## Autor

[Jan Weis](https://github.com/Weisjan)
