#coding:utf-8
from abc import ABC, abstractmethod

class PrinterTicket(ABC):
    
    @abstractmethod
    def printTicket(self) :
        pass
    