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
        print("Vérification : ERREUR")    """
    Décompresse un texte compressé avec la méthode RLE (Run-Length Encoding).
    
    Args:
        texte_compresse (str): Le texte compressé
        
    Returns:
        str: Le texte décompressé
    """
    if not texte_compresse:
        return ""
    
    texte_decompresse = []
    i = 0
    
    # Parcourir la chaîne compressée
    while i < len(texte_compresse):
        # Le caractère courant
        caractere = texte_compresse[i]
        
        # Vérifier si le prochain caractère est un chiffre
        if i + 1 < len(texte_compresse) and texte_compresse[i + 1].isdigit():
            # Extraire le nombre complet (peut avoir plusieurs chiffres)
            j = i + 1
            nombre_str = ""
            
            while j < len(texte_compresse) and texte_compresse[j].isdigit():
                nombre_str += texte_compresse[j]
                j += 1
            
            # Répéter le caractère le nombre de fois indiqué
            nombre = int(nombre_str)
            texte_decompresse.append(caractere * nombre)
            
            # Avancer l'index
            i = j
        else:
            # Pas de nombre : caractère unique
            texte_decompresse.append(caractere)
            i += 1
    
    return ''.join(texte_decompresse)


# Exemple d'utilisation
if __name__ == "__main__":
    # Test avec l'exemple donné
    texte_original = "aaabbcccc"
    texte_compresse = compresser_texte(texte_original)
    
    print(f"Texte original  : {texte_original}")
    print(f"Texte compressé : {texte_compresse}")
    
    # Test de décompression
    texte_decompresse = decompresser_texte(texte_compresse)
    print(f"Texte décompressé : {texte_decompresse}")
    
    # Vérification
    print(f"Vérification : {'OK' if texte_original == texte_decompresse else 'ERREUR'}")
    
    # Autres exemples
    tests = [
        "abcd",
        "aabbccdd",
        "aaaaa",
        "a" * 10 + "b" * 5 + "c",
        "abcccddeeeeeffff"
    ]
    
    print("\n--- Tests supplémentaires ---")
    for test in tests:
        compresse = compresser_texte(test)
        decompresse = decompresser_texte(compresse)
        ratio = len(compresse) / len(test) * 100 if test else 0
        
        print(f"Original  : {test}")
        print(f"Compressé : {compresse}")
        print(f"Ratio     : {ratio:.1f}%")
        print(f"Vérif     : {'✓' if test == decompresse else '✗'}")
        print("-" * 30)

