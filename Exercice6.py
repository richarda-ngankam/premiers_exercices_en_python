# 6. Construisez un DataFrame pandas contenant les notes de 3 matières
# pour une dizaine d'étudiants fictifs, calculez leur matrice de
# corrélation avec .corr(), et affichez-la avec sns.heatmap(annot=True).

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

notes_df = pd.DataFrame({
    "Mathématiques": [12, 14, 10, 16, 15, 9, 13, 17, 11, 18],
    "Informatique": [14, 16, 11, 18, 17, 10, 15, 19, 12, 20],
    "Anglais": [10, 12, 13, 14, 11, 15, 12, 16, 14, 17]
})

correlation = notes_df.corr()

sns.heatmap(correlation, annot=True)

plt.title("Corrélation entre les notes des matières")
plt.show()