# 1. À partir d'une liste de notes, utilisez une boucle for pour compter combien de notes sont
# supérieures ou égales à 10.

notes = [8, 12, 15, 17, 10, 6, 14]
nombre_notes_valides = 0

for note in notes:
    if note >= 10:
        nombre_notes_valides += 1

print("Nombre de notes supérieures ou égales à 10 :", nombre_notes_valides)


# 2. Écrivez une boucle for qui parcourt une liste de notes et affiche "ÉCHEC" si la note est inférieure à
# 10, "MENTION" si elle est supérieure ou égale à 14, et "PASSABLE" sinon.
# notes = [8, 12, 15, 17, 10, 6]

notes = [8, 12, 15, 17, 10, 6]

for note in notes:
    if note < 10:
        print(note, ":", "ÉCHEC")
    elif note >= 14:
        print(note, ":", "MENTION")
    else:
        print(note, ":", "PASSABLE")


# 3. Simulez, avec une boucle while, la progression d'un étudiant dont le score de départ est de 40
# points et augmente de 3 % par semaine, jusqu'à ce qu'il dépasse 60 points. Affichez le nombre de
# semaines nécessaires.

score = 40
semaine = 0

while score <= 60:
    score = score * 1.03
    semaine += 1

print("Nombre de semaines nécessaires :", semaine)
print("Score final :", score)


# 4. Combinez for et une comparaison : à partir de deux listes de même longueur notes_cc et
# notes_examen, affichez pour chaque étudiant "PROGRESSION" si notes_examen[i] > notes_cc[i],
# sinon "PAS DE PROGRESSION".

notes_cc = [10, 12, 14, 9, 15]
notes_examen = [13, 11, 16, 9, 17]

for i in range(len(notes_cc)):
    if notes_examen[i] > notes_cc[i]:
        print(f"Étudiant {i + 1} : PROGRESSION")
    else:
        print(f"Étudiant {i + 1} : PAS DE PROGRESSION")