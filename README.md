# Readme - Flappy Bird

Tento kód implementuje jednoduchou verzi hry "Flappy Bird" pomocí knihovny Pygame v programovacím jazyce Python. Níže jsou uvedeny klíčové prvky a funkce kódu.

### Hlavní Funkce

1. **Inicializace a Nastavení Okna**
    - Pygame je inicializován a nastaveno okno hry s názvem "Flappy Bird".
    
2. **Herní Proměnné**
    - Definice proměnných jako posun pozadí, rychlost posunu, skóre, a další.
    
3. **Třídy**
    - **Pták:** Reprezentuje hlavní postavu hry - ptáka, umožňuje mu pohyb a interakci.
    - **Trubka:** Definuje trubky, kterými musí hráč projít. 
    - **Tlačítko:** Implementuje tlačítko pro restart hry.

4. **Funkce pro Vykreslení Textu a Restart Hry**
    - `vykreslení_textu`: Vykresluje text na obrazovku.
    - `reset_hry`: Resetuje herní proměnné a umožňuje restart hry.

5. **Hlavní Smyčka**
    - Obsahuje hlavní herní smyčku, která řídí průběh hry.
    - Zahrnuje vykreslování pozadí, aktualizaci pozic objektů, kontrolu kolizí, skóre a stavu hry, generování nových trubek a interakci s uživatelem.

6. **Konec Hry a Restart**
    - Po detekci konce hry je zobrazeno tlačítko pro restart.
    - Při kliknutí na tlačítko je hra resetována a může se hrát znovu.

### Obrázky a Fonty
- Kód používá obrázky pro pozadí, ptáka, trubky a tlačítko restartu.
- Pro textové zprávy je použit font "Bauhaus 93".

### Ovládání
- Hra reaguje na kliknutí myší, kdy hráč ovládá skok ptáka.

### Autor
- Tento kód byl vytvořen s pomocí Pygame a Pythonu autorem [uváděj jméno autora].

### Instalace
1. Nainstalujte Python a Pygame.
2. Stáhněte zdrojový kód a obrázky.
3. Spusťte soubor `rocnikovy_projekt_Dostál.py`.

Tento readme soubor poskytuje základní informace o implementaci této verze "Flappy Bird" hry. Pro další detaily se podívejte přímo do kódu. Hodně zábavy při hraní!
