# 1. À partir d'une liste de 10 notes et d'une liste de 10 évaluations (sous forme de chaînes), tracez la
# courbe des notes avec plt.plot(), en ajoutant un titre et des labels d'axes.

import matplotlib.pyplot as plt

evaluations = [
    "Éval 1", "Éval 2", "Éval 3", "Éval 4", "Éval 5",
    "Éval 6", "Éval 7", "Éval 8", "Éval 9", "Éval 10"
]

notes = [12, 14, 13, 15, 16, 11, 17, 14, 15, 18]

plt.plot(evaluations, notes, marker="o")
plt.title("Évolution des notes")
plt.xlabel("Évaluations")
plt.ylabel("Notes sur 20")
plt.show()


# 2. Sur le même graphique, ajoutez une deuxième courbe représentant une moyenne glissante sur 3
# évaluations (vous pouvez la calculer avec une boucle for, voir 5.1), avec une légende distinguant les
# deux courbes.

moyennes_glissantes = []

for i in range(2, len(notes)):
    moyenne = (notes[i - 2] + notes[i - 1] + notes[i]) / 3
    moyennes_glissantes.append(moyenne)

evaluations_moyennes = evaluations[2:]

plt.plot(evaluations, notes, marker="o", label="Notes")
plt.plot(evaluations_moyennes, moyennes_glissantes, marker="s", label="Moyenne glissante")

plt.title("Notes et moyennes glissantes")
plt.xlabel("Évaluations")
plt.ylabel("Notes sur 20")
plt.legend()
plt.show()


# 3. Tracez un graphique en barres du nombre d'étudiants par filière à partir d'une liste d'effectifs,
# avec plt.bar().

filieres = ["Génie Logiciel", "Réseaux", "Comptabilité", "Marketing"]
effectifs = [45, 30, 35, 25]

plt.bar(filieres, effectifs)

plt.title("Nombre d'étudiants par filière")
plt.xlabel("Filières")
plt.ylabel("Nombre d'étudiants")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()


# 4. Créez deux sous-graphiques verticaux (plt.subplots(2, 1)) affichant respectivement les notes et le
# taux de présence, avec un axe des semaines partagé (sharex=True).

semaines = [1, 2, 3, 4, 5, 6]
notes = [12, 14, 13, 16, 15, 17]
presence = [80, 85, 90, 75, 95, 100]

fig, axes = plt.subplots(2, 1, sharex=True)

axes[0].plot(semaines, notes, marker="o")
axes[0].set_title("Évolution des notes")
axes[0].set_ylabel("Note sur 20")

axes[1].plot(semaines, presence, marker="s")
axes[1].set_title("Taux de présence")
axes[1].set_ylabel("Présence (%)")
axes[1].set_xlabel("Semaines")

plt.tight_layout()
plt.show()


# 5. À partir d'une liste de notes, tracez un histogramme de leur distribution avec sns.histplot(), avec
# kde=True.

import seaborn as sns

notes = [8, 10, 12, 14, 15, 16, 12, 13, 17, 18, 9, 11, 14, 15, 16]

sns.histplot(notes, bins=10, kde=True)

plt.title("Distribution des notes")
plt.xlabel("Notes sur 20")
plt.ylabel("Effectif")
plt.show()


# 6. Construisez un DataFrame pandas contenant les notes de 3 matières pour une dizaine d'étudiants
# fictifs, calculez leur matrice de corrélation avec .corr(), et affichez-la avec sns.heatmap(annot=True).

import pandas as pd

notes_df = pd.DataFrame({
    "Mathématiques": [12, 14, 10, 16, 15, 9, 13, 17, 11, 18],
    "Informatique": [14, 16, 11, 18, 17, 10, 15, 19, 12, 20],
    "Anglais": [10, 12, 13, 14, 11, 15, 12, 16, 14, 17]
})

correlation = notes_df.corr()

sns.heatmap(correlation, annot=True, cmap="Blues", fmt=".2f")

plt.title("Corrélation entre les notes des matières")
plt.show()