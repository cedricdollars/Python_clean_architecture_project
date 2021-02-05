#coding:utf-8
from abc import ABC, abstractmethod
from domain.entities.car import Car

class AddCarParking(ABC):
    
    @abstractmethod
    def add_car(self, car: Car) -> bool:
        pass