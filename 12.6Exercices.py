# 1. Créez une classe Etudiant avec un constructeur (nom, note_cc, note_examen) et une méthode
# moyenne() qui renvoie la moyenne pondérée (40 % contrôle continu, 60 % examen).

class Etudiant:
    def __init__(self, nom, note_cc, note_examen):
        self.nom = nom
        self.note_cc = note_cc
        self.note_examen = note_examen

    def moyenne(self):
        return self.note_cc * 0.4 + self.note_examen * 0.6


amina = Etudiant("Amina", 12, 15)
print("Moyenne :", amina.moyenne())


# 2. Ajoutez une méthode afficher() qui affiche une ligne résumant l'étudiant (nom, note de contrôle
# continu, note d'examen).

class Etudiant:
    def __init__(self, nom, note_cc, note_examen):
        self.nom = nom
        self.note_cc = note_cc
        self.note_examen = note_examen

    def moyenne(self):
        return self.note_cc * 0.4 + self.note_examen * 0.6

    def afficher(self):
        print(
            f"{self.nom} | Contrôle continu : {self.note_cc} | "
            f"Examen : {self.note_examen}"
        )


amina = Etudiant("Amina", 12, 15)
amina.afficher()


# 3. Créez une classe Groupe contenant une liste d'objets Etudiant, avec une méthode
# ajouter(etudiant) et une méthode moyenne_generale() (voir l'exemple de la section 12.4).

class Etudiant:
    def __init__(self, nom, note_cc, note_examen):
        self.nom = nom
        self.note_cc = note_cc
        self.note_examen = note_examen

    def moyenne(self):
        return self.note_cc * 0.4 + self.note_examen * 0.6


class Groupe:
    def __init__(self):
        self.etudiants = []

    def ajouter(self, etudiant):
        self.etudiants.append(etudiant)

    def moyenne_generale(self):
        if len(self.etudiants) == 0:
            return 0

        total = 0

        for etudiant in self.etudiants:
            total += etudiant.moyenne()

        return total / len(self.etudiants)


groupe = Groupe()
groupe.ajouter(Etudiant("Amina", 12, 15))
groupe.ajouter(Etudiant("Brice", 10, 11))
groupe.ajouter(Etudiant("Chloé", 14, 16))

print("Moyenne générale :", groupe.moyenne_generale())


# 4. Créez une classe Delegue héritant de Etudiant, ajoutant un attribut filiere et une méthode
# presenter() qui renvoie une phrase indiquant le nom du délégué et sa filière.

class Etudiant:
    def __init__(self, nom, note_cc, note_examen):
        self.nom = nom
        self.note_cc = note_cc
        self.note_examen = note_examen

    def moyenne(self):
        return self.note_cc * 0.4 + self.note_examen * 0.6


class Delegue(Etudiant):
    def __init__(self, nom, note_cc, note_examen, filiere):
        super().__init__(nom, note_cc, note_examen)
        self.filiere = filiere

    def presenter(self):
        return f"{self.nom} est délégué de la filière {self.filiere}."


delegue = Delegue("Amina", 12, 15, "Génie Logiciel")
print(delegue.presenter())


# 5. Testez votre classe Groupe avec au moins 3 étudiants différents, et affichez l'étudiant qui a la
# meilleure moyenne à l'aide d'une boucle for et d'une comparaison (voir 5.2).

class Etudiant:
    def __init__(self, nom, note_cc, note_examen):
        self.nom = nom
        self.note_cc = note_cc
        self.note_examen = note_examen

    def moyenne(self):
        return self.note_cc * 0.4 + self.note_examen * 0.6


class Groupe:
    def __init__(self):
        self.etudiants = []

    def ajouter(self, etudiant):
        self.etudiants.append(etudiant)

    def moyenne_generale(self):
        if not self.etudiants:
            return 0

        total = 0
        for etudiant in self.etudiants:
            total += etudiant.moyenne()

        return total / len(self.etudiants)


groupe = Groupe()

groupe.ajouter(Etudiant("Amina", 12, 15))
groupe.ajouter(Etudiant("Brice", 10, 11))
groupe.ajouter(Etudiant("Chloé", 14, 16))

meilleur_etudiant = groupe.etudiants[0]

for etudiant in groupe.etudiants:
    if etudiant.moyenne() > meilleur_etudiant.moyenne():
        meilleur_etudiant = etudiant

print("Étudiant ayant la meilleure moyenne :", meilleur_etudiant.nom)
print("Meilleure moyenne :", meilleur_etudiant.moyenne())