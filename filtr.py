from PIL import Image

# Načtení obrázku
obrazek = Image.open("kitten.jpg")
sirka, vyska = obrazek.size

# Přechod přes každý pixel
for x in range(sirka):
    for y in range(vyska):
        # Získání hodnoty pixelu (R, G, B)
        r, g, b = obrazek.getpixel((x, y))
        
        # Inverze barev
        new_r = 255 - r
        new_g = 255 - g
        new_b = 255 - b
        
        # Nastavení nových hodnot pixelu
        obrazek.putpixel((x, y), (new_r, new_g, new_b))

# Zobrazení upraveného obrázku
obrazek.show()
