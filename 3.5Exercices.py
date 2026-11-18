# 1. Affichez, à l'aide d'une f-string, la phrase suivante en remplaçant les valeurs par des variables :
# « Le serveur de l'école stocke 3.10e+12 octets de données pour 412 étudiants inscrits. »

capacite = 3.10e12
nombre_etudiants = 412

print(f"Le serveur de l'école stocke {capacite:.2e} octets de données pour {nombre_etudiants} étudiants inscrits.")


# 2. Corrigez le script suivant qui provoque une erreur TypeError :
# nb_etudiants = "50"
# temps_par_copie = 12.4
# temps_total = nb_etudiants * temps_par_copie
# print(temps_total)

nb_etudiants = "50"
temps_par_copie = 12.4

nb_etudiants = int(nb_etudiants)
temps_total = nb_etudiants * temps_par_copie

print("Temps total :", temps_total)


# 3. Affichez un relevé à deux lignes pour deux étudiants (nom, crédits, note), alignées en colonnes à
# l'aide des spécificateurs <, > et .2f.

nom1 = "Amina"
credits1 = 30
note1 = 14.75

nom2 = "Brice"
credits2 = 24
note2 = 12.50

print(f"{'Nom':<10}{'Crédits':>10}{'Note':>10}")
print(f"{nom1:<10}{credits1:>10}{note1:>10.2f}")
print(f"{nom2:<10}{credits2:>10}{note2:>10.2f}")