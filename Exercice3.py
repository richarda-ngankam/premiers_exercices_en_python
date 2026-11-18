# 3. Tracez un graphique en barres du nombre d'étudiants par filière
# à partir d'une liste d'effectifs, avec plt.bar().

import matplotlib.pyplot as plt

filieres = ["Génie Logiciel", "Réseaux", "Comptabilité", "Marketing"]
effectifs = [45, 30, 35, 25]

plt.bar(filieres, effectifs)

plt.title("Nombre d'étudiants par filière")
plt.xlabel("Filières")
plt.ylabel("Nombre d'étudiants")
plt.show()