#coding:utf-8
from abc import ABC, abstractmethod

class AjoutVoitureDansLeParking(ABC):
    
    @abstractmethod
    def ajouter_une_voiture(self, num_matricule:str, modele:str, couleur:str):
        pass
    
    @abstractmethod
    def autoriser_ajout_voiture(self, num_matricule:str, modele:str, couleur:str):
        pass