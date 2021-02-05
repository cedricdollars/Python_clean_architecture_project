#coding:utf-8
from abc import ABC, abstractmethod

class MakingAvailablePlace(ABC):
    
    @abstractmethod
    def make_available_place(self, numero_place:int):
        pass
    