# EXERCICE 1. Créez une classe abstraite Animal avec une méthode abstraite crier() et une méthode
# concrète se_presenter() qui affiche le nom et le cri. Implémentez Chien et Chat.

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nom):
        self.nom = nom

    @abstractmethod
    def crier(self):
        pass

    def se_presenter(self):
        print(f"Je m'appelle {self.nom} et je fais : {self.crier()}")


class Chien(Animal):
    def crier(self):
        return "Wouf !"


class Chat(Animal):
    def crier(self):
        return "Miaou !"


chien = Chien("Max")
chat = Chat("Minou")

chien.se_presenter()
chat.se_presenter()


# EXERCICE 2. Définissez une interface Stockage (sauvegarder(cle, valeur), charger(cle)),
# puis implémentez StockageMemoire (dictionnaire) et StockageFichier (JSON).

from abc import ABC, abstractmethod
import json
import os


class Stockage(ABC):
    @abstractmethod
    def sauvegarder(self, cle, valeur):
        pass

    @abstractmethod
    def charger(self, cle):
        pass


class StockageMemoire(Stockage):
    def __init__(self):
        self.donnees = {}

    def sauvegarder(self, cle, valeur):
        self.donnees[cle] = valeur

    def charger(self, cle):
        return self.donnees.get(cle)


class StockageFichier(Stockage):
    def __init__(self, chemin="donnees.json"):
        self.chemin = chemin

    def sauvegarder(self, cle, valeur):
        if os.path.exists(self.chemin):
            with open(self.chemin, "r", encoding="utf-8") as fichier:
                donnees = json.load(fichier)
        else:
            donnees = {}

        donnees[cle] = valeur

        with open(self.chemin, "w", encoding="utf-8") as fichier:
            json.dump(donnees, fichier, ensure_ascii=False, indent=4)

    def charger(self, cle):
        if not os.path.exists(self.chemin):
            return None

        with open(self.chemin, "r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)

        return donnees.get(cle)


# Test de StockageMemoire

stockage_memoire = StockageMemoire()

stockage_memoire.sauvegarder("nom", "Amina")
stockage_memoire.sauvegarder("age", 20)

print("Nom :", stockage_memoire.charger("nom"))
print("Âge :", stockage_memoire.charger("age"))


# Test de StockageFichier

stockage_fichier = StockageFichier()

stockage_fichier.sauvegarder("nom", "Brice")
stockage_fichier.sauvegarder("moyenne", 14.5)

print("Nom enregistré :", stockage_fichier.charger("nom"))
print("Moyenne enregistrée :", stockage_fichier.charger("moyenne"))


# EXERCICE 3. Écrivez un Protocol nommé Comparable avec la méthode comparer(autre) -> int,
# puis une fonction plus_grand(a, b) qui l'utilise.

from typing import Protocol


class Comparable(Protocol):
    def comparer(self, autre) -> int:
        ...


def plus_grand(a: Comparable, b: Comparable):
    if a.comparer(b) > 0:
        return a
    else:
        return b


class Nombre:
    def __init__(self, valeur):
        self.valeur = valeur

    def comparer(self, autre) -> int:
        if self.valeur > autre.valeur:
            return 1
        elif self.valeur < autre.valeur:
            return -1
        else:
            return 0


nombre1 = Nombre(15)
nombre2 = Nombre(20)

resultat = plus_grand(nombre1, nombre2)

print("Le plus grand nombre est :", resultat.valeur)


# EXERCICE 4 (réflexion). Pour un système de paiement e-commerce (Mobile Money, carte, cash à la
# livraison), proposez une conception avec une interface et une classe abstraite. Justifiez votre choix.

from abc import ABC, abstractmethod


# L'interface Payable définit le contrat que chaque moyen de paiement doit respecter.

class Payable(ABC):
    @abstractmethod
    def payer(self):
        pass


# La classe abstraite Paiement contient les éléments communs aux moyens de paiement.
# Elle conserve le montant et fournit une méthode commune de traitement.
# Chaque classe fille doit implémenter sa propre méthode payer().

class Paiement(Payable, ABC):
    def __init__(self, montant):
        self._montant = montant

    def traiter(self):
        if self._montant <= 0:
            print("Montant invalide.")
            return

        self.payer()


class PaiementMobileMoney(Paiement):
    def payer(self):
        print(f"Paiement Mobile Money de {self._montant} FCFA effectué.")


class PaiementCarte(Paiement):
    def payer(self):
        print(f"Paiement par carte de {self._montant} FCFA effectué.")


class PaiementLivraison(Paiement):
    def payer(self):
        print(f"Paiement de {self._montant} FCFA prévu à la livraison.")


# Chaque moyen de paiement utilise le même contrat, mais possède son propre comportement.

paiements = [
    PaiementMobileMoney(15000),
    PaiementCarte(25000),
    PaiementLivraison(10000)
]

for paiement in paiements:
    paiement.traiter()


# Justification :
# L'interface Payable impose une méthode payer() à toutes les classes.
# La classe abstraite Paiement regroupe les éléments communs, notamment le montant
# et le traitement du paiement.
# Les classes filles définissent le comportement propre à chaque moyen de paiement.


# EXERCICE 5 (encapsulation). Écrivez une classe Etudiant avec un attribut privé __notes (liste),
# une méthode ajouter_note(note) qui refuse toute note hors de [0, 20], et une propriété en lecture
# seule moyenne. Vérifiez que etudiant.moyenne = 15 lève une erreur.

class Etudiant:
    def __init__(self):
        self.__notes = []

    def ajouter_note(self, note):
        if note < 0 or note > 20:
            raise ValueError("La note doit être comprise entre 0 et 20.")

        self.__notes.append(note)

    @property
    def moyenne(self):
        if len(self.__notes) == 0:
            return 0

        return sum(self.__notes) / len(self.__notes)


# Création d'un étudiant et ajout de notes.

etudiant = Etudiant()

etudiant.ajouter_note(12)
etudiant.ajouter_note(15)
etudiant.ajouter_note(18)

print("Moyenne de l'étudiant :", etudiant.moyenne)


# Vérification du refus d'une note invalide.

try:
    etudiant.ajouter_note(25)
except ValueError as erreur:
    print("Erreur :", erreur)


# Vérification que la propriété moyenne est en lecture seule.

try:
    etudiant.moyenne = 15
except AttributeError as erreur:
    print("Erreur :", erreur)