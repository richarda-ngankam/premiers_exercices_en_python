# 2. Sur le même graphique, ajoutez une deuxième courbe représentant
# une moyenne glissante sur 3 évaluations (vous pouvez la calculer
# avec une boucle for, voir 5.1), avec une légende distinguant les deux courbes.

import matplotlib.pyplot as plt

evaluations = [
    "Éval 1", "Éval 2", "Éval 3", "Éval 4", "Éval 5",
    "Éval 6", "Éval 7", "Éval 8", "Éval 9", "Éval 10"
]

notes = [12, 14, 13, 15, 16, 11, 17, 14, 15, 18]

moyennes_glissantes = []

for i in range(2, len(notes)):
    moyenne = (notes[i - 2] + notes[i - 1] + notes[i]) / 3
    moyennes_glissantes.append(moyenne)

plt.plot(evaluations, notes, label="Notes")
plt.plot(evaluations[2:], moyennes_glissantes, label="Moyenne glissante")

plt.title("Notes et moyennes glissantes")
plt.xlabel("Évaluations")
plt.ylabel("Notes sur 20")
plt.legend()
plt.show()