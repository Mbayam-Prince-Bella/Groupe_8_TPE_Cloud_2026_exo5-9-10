import re  # Module pour les expressions régulières

def est_palindrome_phrase(phrase):
    # Supprime tout ce qui n'est pas une lettre
    phrase_nettoyee = re.sub(r'[^a-zA-Z]', '', phrase)
    
    # Met en minuscules
    phrase_nettoyee = phrase_nettoyee.lower()
    
    # Compare avec l'inverse
    return phrase_nettoyee == phrase_nettoyee[::-1]


# Programme principal
if __name__ == "__main__":
    phrase_utilisateur = input("Entrez un mot ou une phrase : ")

    if est_palindrome_phrase(phrase_utilisateur):
        print(f'"{phrase_utilisateur}" est un palindrome !')
    else:
        print(f'"{phrase_utilisateur}" n\'est pas un palindrome.')
