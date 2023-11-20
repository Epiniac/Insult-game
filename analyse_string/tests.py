import spacy

# Charger le modèle linguistique pour l'anglais
nlp = spacy.load("en_core_web_sm")

def has_syntax_errors(text):
    # Traitement du texte avec spaCy
    doc = nlp(text)

    # Vérification de la présence d'erreurs syntaxiques
    for token in doc:
        if token.dep_ in ('amod', 'nsubj', 'nsubjpass', 'advmod', 'attr'):
            return False 

    # Aucune erreur syntaxique détectée
    return True

# Exemple d'utilisation
text_to_analyze = "Plane like I."
result = has_syntax_errors(text_to_analyze)

# Affichage du résultat
print(result)

