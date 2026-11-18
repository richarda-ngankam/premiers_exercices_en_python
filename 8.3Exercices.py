# 1. Créez un dictionnaire etudiant décrivant un étudiant (nom, âge, filière, moyenne), puis affichez
# chaque information avec une f-string.

etudiant = {
    "nom": "Amina",
    "age": 20,
    "filiere": "Génie Logiciel",
    "moyenne": 14.5
}

print(f"Nom : {etudiant['nom']}")
print(f"Âge : {etudiant['age']} ans")
print(f"Filière : {etudiant['filiere']}")
print(f"Moyenne : {etudiant['moyenne']}")


# 2. À partir d'une liste de dictionnaires représentant une classe (nom, note_cc, note_examen),
# calculez la moyenne de chaque étudiant (40 % contrôle continu, 60 % examen) puis la moyenne
# générale de la classe à l'aide d'une boucle for.

classe = [
    {"nom": "Amina", "note_cc": 12, "note_examen": 15},
    {"nom": "Brice", "note_cc": 10, "note_examen": 11},
    {"nom": "Chloé", "note_cc": 14, "note_examen": 16}
]

total_moyennes = 0

for etudiant in classe:
    moyenne = etudiant["note_cc"] * 0.4 + etudiant["note_examen"] * 0.6
    total_moyennes += moyenne
    print(f"{etudiant['nom']} : {moyenne:.2f} / 20")

moyenne_generale = total_moyennes / len(classe)

print("Moyenne générale de la classe :", moyenne_generale)


# 3. Créez un tuple (note_min, note_max, moyenne) pour 3 étudiants différents (donc 3 tuples), et
# affichez pour chacun l'écart (note_max - note_min).

amina = (10, 18, 14)
brice = (8, 15, 11.5)
chloe = (12, 19, 16)

etudiants = {
    "Amina": amina,
    "Brice": brice,
    "Chloé": chloe
}

for nom, bulletin in etudiants.items():
    note_min, note_max, moyenne = bulletin
    ecart = note_max - note_min
    print(f"{nom} : écart de {ecart} points")


# 4. Utilisez .get() pour tenter de lire une clé "mention" absente d'un dictionnaire etudiant, en
# renvoyant "aucune" par défaut.

etudiant = {
    "nom": "Amina",
    "age": 20,
    "moyenne": 14.5
}

mention = etudiant.get("mention", "aucune")

print("Mention :", mention)