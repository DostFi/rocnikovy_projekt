# Editor fotografií - Nápověda

Tento skript v Pythonu umožňuje uživatelům provádět různé úpravy obrázků s použitím nabízených možností v menu.

## Požadavky

- Python 3.x
- PIL (Python Imaging Library)

## Použití

1. Ujistěte se, že máte nainstalovaný Python a PIL ve vašem systému.
2. Spusťte skript (`photo_editor.py`).
3. Budete představeni nabídkou, kde můžete vybrat různé úpravy obrázků.
4. Postupujte podle pokynů na obrazovce pro provedení požadované úpravy.
5. Chcete-li ukončit program, vyberte možnost 0.

## Dostupné úpravy

1. **Rozmazání:** Aplikuje rozmazání na obrázek.
2. **Konturování:** Aplikuje efekt kontur na obrázek.
3. **Detaily:** Zvyšuje detaily v obrázku.
4. **Zesílení hran:** Zvyšuje hrany objektů na obrázku.
5. **Reliéf:** Aplikuje reliéfní efekt na obrázek.
6. **Detekce hran:** Detekuje hrany v obrázku pomocí předdefinovaného filtru.

## Soubory

- `photo_editor.py`: Hlavní Python skript.
- `opice.jpg`: Ukázkový obrázkový soubor (můžete ho nahradit vlastním obrázkem).

## Funkce

- `detekce_okraje(obraz)`: Tato funkce detekuje hrany v poskytnutém obrázku pomocí předdefinovaného filtru.

## Poznámka

Ujistěte se, že soubor s obrázkem (`opice.jpg`) je ve stejném adresáři jako skript.

Tento skript využívá knihovnu PIL k zpracování obrázků. Pokud ji nemáte nainstalovanou, můžete ji nainstalovat pomocí pip: `pip install pillow`.

## Přispěvatelé

- Filip Dostál

