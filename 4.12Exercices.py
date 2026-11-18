# 1. Créez une liste notes contenant les 6 dernières notes d'un étudiant de votre choix, puis affichez la
# première, la dernière, et les 3 premières à l'aide d'une tranche.

notes = [12, 14, 15, 11, 16, 13]

print("Première note :", notes[0])
print("Dernière note :", notes[-1])
print("Les trois premières notes :", notes[:3])


# 2. Calculez et affichez la plus haute, la plus basse et la moyenne de cette liste.

plus_haute = max(notes)
plus_basse = min(notes)
moyenne = sum(notes) / len(notes)

print("Plus haute note :", plus_haute)
print("Plus basse note :", plus_basse)
print("Moyenne :", moyenne)


# 3. Ajoutez une nouvelle note en fin de liste avec .append(), puis retirez la plus ancienne (indice 0)
# avec .pop(0).

notes.append(17)
print("Après ajout :", notes)

note_retiree = notes.pop(0)

print("Note retirée :", note_retiree)
print("Liste mise à jour :", notes)


# 4. Créez une liste de listes représentant 3 étudiants (nom, âge, moyenne), puis affichez le nom du 2e
# étudiant et calculez la moyenne générale des trois.

etudiants = [
    ["Amina", 20, 14.5],
    ["Brice", 21, 12.0],
    ["Chloé", 19, 16.0]
]

print("Nom du deuxième étudiant :", etudiants[1][0])

moyenne_generale = (
    etudiants[0][2] + etudiants[1][2] + etudiants[2][2]
) / len(etudiants)

print("Moyenne générale :", moyenne_generale)


# 5. Créez une liste, copiez-la avec .copy(), modifiez la copie, et vérifiez que l'originale n'a pas changé.

notes_originales = [12, 14, 15, 16]
notes_copie = notes_originales.copy()

notes_copie.append(18)
notes_copie[0] = 10

print("Liste originale :", notes_originales)
print("Liste copiée et modifiée :", notes_copie)