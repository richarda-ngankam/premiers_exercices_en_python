# 1. Créez des variables note_cc (12), note_examen (15) et coef_examen (0.6), puis calculez la
# moyenne pondérée : note_cc * (1 - coef_examen) + note_examen * coef_examen.

note_cc = 12
note_examen = 15
coef_examen = 0.6

moyenne = note_cc * (1 - coef_examen) + note_examen * coef_examen
print("Moyenne pondérée :", moyenne)


# 2. Un enseignant a corrigé 15 copies et la somme de toutes les notes vaut 187.5. Calculez la
# moyenne de la classe, puis son écart avec la note de validation 10.

nombre_copies = 15
somme_notes = 187.5
note_validation = 10

moyenne_classe = somme_notes / nombre_copies
ecart = moyenne_classe - note_validation

print("Moyenne de la classe :", moyenne_classe)
print("Écart avec la note de validation :", ecart)


# 3. Créez une variable note_str = "16.75" (texte) et convertissez-la en float pour pouvoir la multiplier
# par 3.

note_str = "16.75"
note = float(note_str)
resultat = note * 3

print("Résultat :", resultat)


# 4. Deux étudiants ont obtenu 15.10 et 15.04 au même examen. À l'aide de max(), affichez la
# meilleure note.

note_etudiant_1 = 15.10
note_etudiant_2 = 15.04

meilleure_note = max(note_etudiant_1, note_etudiant_2)

print("Meilleure note :", meilleure_note)