def compresser_texte(texte):
    if not texte:
        return ""

    texte_compresse = []
    caractere_courant = texte[0]
    compteur = 1

    for i in range(1, len(texte)):
        if texte[i] == caractere_courant:
            compteur += 1
        else:
            texte_compresse.append(caractere_courant)
            if compteur > 1:
                texte_compresse.append(str(compteur))
            caractere_courant = texte[i]
            compteur = 1

    texte_compresse.append(caractere_courant)
    if compteur > 1:
        texte_compresse.append(str(compteur))

    return ''.join(texte_compresse)


def decompresser_texte(texte_compresse):
    if not texte_compresse:
        return ""

    texte_decompresse = []
    i = 0

    while i < len(texte_compresse):
        caractere = texte_compresse[i]

        if i + 1 < len(texte_compresse) and texte_compresse[i + 1].isdigit():
            j = i + 1
            nombre_str = ""

            while j < len(texte_compresse) and texte_compresse[j].isdigit():
                nombre_str += texte_compresse[j]
                j += 1

            texte_decompresse.append(caractere * int(nombre_str))
            i = j
        else:
            texte_decompresse.append(caractere)
            i += 1

    return ''.join(texte_decompresse)


# Programme principal
if __name__ == "__main__":
    texte_original = input("Entrez une chaîne de caractères à compresser : ")

    texte_compresse = compresser_texte(texte_original)
    texte_decompresse = decompresser_texte(texte_compresse)

    print("\nRésultats :")
    print(f"Texte original     : {texte_original}")
    print(f"Texte compressé    : {texte_compresse}")
    print(f"Texte décompressé  : {texte_decompresse}")

    if texte_original == texte_decompresse:
        print("Vérification : OK")
    else:
        print("Vérification : ERREUR")
