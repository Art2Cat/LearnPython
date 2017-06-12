#!/usr/bin/env python3
class Animal(object):
    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def run(self):
        print('Animal is running...')

    def introduce(self):
        print('%s is %s Animal!!!' % (self.get_name(), self.get_color()))
