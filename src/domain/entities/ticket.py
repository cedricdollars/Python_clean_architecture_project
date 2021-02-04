#coding:utf-8

class Ticket(object):
    def __init__(self, number_of_place, date_arrived, car_info):
        self.number_of_place = number_of_place
        self.date_arrived = date_arrived
        self.car_info = car_info