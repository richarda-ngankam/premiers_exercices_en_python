# 5. À partir d'une liste de notes, tracez un histogramme de leur
# distribution avec sns.histplot(), avec kde=True.

import seaborn as sns
import matplotlib.pyplot as plt

notes = [8, 10, 12, 14, 15, 16, 12, 13, 17, 18, 9, 11, 14, 15, 16]

sns.histplot(notes, kde=True)

plt.title("Distribution des notes")
plt.xlabel("Notes sur 20")
plt.ylabel("Effectif")
plt.show()