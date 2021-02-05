#coding:utf-8
from abc import ABC, abstractmethod

class MakingUnvavailablePlace(ABC):
    
    @abstractmethod
    def make_unavailable_place(self, numero_place:int):
        pass