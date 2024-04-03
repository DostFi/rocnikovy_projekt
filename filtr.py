from PIL import Image, ImageFilter

def detekce_okraje(obraz):
    obraz_odstiny = obraz.convert("L")
    obraz_okraje = obraz_odstiny.filter(ImageFilter.FIND_EDGES)
    return obraz_okraje

while True:
    obraz = Image.open("opice.jpg")
    print("Menu editoru fotografií:")
    print("1. Použít rozmazání")
    print("2. Použít konturování")
    print("3. Použít detailní filtr")
    print("4. Použít zesílení hran")
    print("5. Použít reliéf")
    print("6. Použít detekci hran")
    print("0. Ukončit")

    volba = input("Zadejte svou volbu: ")

    if volba == "1":
        obraz.filter(ImageFilter.BLUR).show()
        print("Rozmazání použito.")
    elif volba == "2":
        obraz.filter(ImageFilter.CONTOUR).show()
        print("Konturování použito.")
    elif volba == "3":
        obraz.filter(ImageFilter.DETAIL).show()
        print("Detailní filtr použit.")
    elif volba == "4":
        obraz.filter(ImageFilter.EDGE_ENHANCE).show()
        print("Filtr zesílení hran použit.")
    elif volba == "5":
        obraz.filter(ImageFilter.EMBOSS).show()
        print("Filtr reliéfu použit.")
    elif volba == "6":
        obraz_okraje = detekce_okraje(obraz)
        obraz_okraje.show()
        print("Detekce hran použita.")
    elif volba == "0":
        print("Ukončuji...")
        break
    else:
        print("Neplatná volba. Zkuste to znovu.")

