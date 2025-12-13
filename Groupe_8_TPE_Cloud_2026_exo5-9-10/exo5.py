def compresser_texte(texte):
    """
    Compresse un texte en remplaçant les lettres répétées par un compteur.
    
    Args:
        texte (str): Le texte à compresser
        
    Returns:
        str: Le texte compressé
    """
    # Cas spécial : chaîne vide
    if not texte:
        return ""
    
    # Initialisation
    texte_compresse = []
    caractere_courant = texte[0]
    compteur = 1
    
    # Parcourir le texte à partir du deuxième caractère
    for i in range(1, len(texte)):
        if texte[i] == caractere_courant:
            # Même caractère : incrémenter le compteur
            compteur += 1
        else:
            # Caractère différent : ajouter la compression du caractère précédent
            texte_compresse.append(caractere_courant)
            if compteur > 1:  # On n'ajoute pas le compteur s'il est égal à 1
                texte_compresse.append(str(compteur))
            
            # Réinitialiser pour le nouveau caractère
            caractere_courant = texte[i]
            compteur = 1
    
    # Ajouter le dernier caractère (et son compteur)
    texte_compresse.append(caractere_courant)
    if compteur > 1:
        texte_compresse.append(str(compteur))
    
    # Retourner la chaîne compressée
    return ''.join(texte_compresse)


def decompresser_texte(texte_compresse):
    """
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
