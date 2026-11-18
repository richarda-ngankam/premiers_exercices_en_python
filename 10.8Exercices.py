# 1. Écrivez une fonction calculer_moyenne_classe(classe) qui prend en argument une liste de
# dictionnaires {"nom", "note_cc", "note_examen"} (voir 8.1) et renvoie la moyenne générale de la
# classe (40 % contrôle continu, 60 % examen).

def calculer_moyenne_classe(classe):
    total = 0

    for etudiant in classe:
        moyenne = etudiant["note_cc"] * 0.4 + etudiant["note_examen"] * 0.6
        total += moyenne

    return total / len(classe)


classe = [
    {"nom": "Amina", "note_cc": 12, "note_examen": 15},
    {"nom": "Brice", "note_cc": 10, "note_examen": 11},
    {"nom": "Chloé", "note_cc": 14, "note_examen": 16}
]

print("Moyenne générale :", calculer_moyenne_classe(classe))


# 2. Écrivez une fonction mention(note, seuil_passable=10, seuil_bien=14) qui renvoie "AJOURNÉ" si
# note < seuil_passable, "BIEN" si note >= seuil_bien, et "PASSABLE" sinon.

def mention(note, seuil_passable=10, seuil_bien=14):
    if note < seuil_passable:
        return "AJOURNÉ"
    elif note >= seuil_bien:
        return "BIEN"
    else:
        return "PASSABLE"


print(mention(8))
print(mention(12))
print(mention(16))


# 3. Écrivez une fonction statistiques(notes) qui renvoie à la fois la moyenne, le minimum et le
# maximum d'une liste de notes, sous forme de tuple.

def statistiques(notes):
    moyenne = sum(notes) / len(notes)
    minimum = min(notes)
    maximum = max(notes)

    return moyenne, minimum, maximum


notes = [12, 14, 15, 9, 17]

moyenne, minimum, maximum = statistiques(notes)

print("Moyenne :", moyenne)
print("Minimum :", minimum)
print("Maximum :", maximum)


# 4. Reprenez un script du chapitre 5 comportant du code dupliqué et refactorez-le en une ou
# plusieurs fonctions, en appliquant le principe DRY.

# On crée une fonction pour éviter de répéter les mêmes conditions.

def afficher_resultat(note):
    if note < 10:
        print("ÉCHEC")
    elif note >= 14:
        print("MENTION")
    else:
        print("PASSABLE")


notes = [8, 12, 15, 17, 10, 6]

for note in notes:
    afficher_resultat(note)