# 1. À partir d'une liste de 10 notes et d'une liste de 10 évaluations
# (sous forme de chaînes), tracez la courbe des notes avec plt.plot(),
# en ajoutant un titre et des labels d'axes.

import matplotlib.pyplot as plt

evaluations = [
    "Éval 1", "Éval 2", "Éval 3", "Éval 4", "Éval 5",
    "Éval 6", "Éval 7", "Éval 8", "Éval 9", "Éval 10"
]

notes = [12, 14, 13, 15, 16, 11, 17, 14, 15, 18]

plt.plot(evaluations, notes)
plt.title("Évolution des notes")
plt.xlabel("Évaluations")
plt.ylabel("Notes sur 20")
plt.show()