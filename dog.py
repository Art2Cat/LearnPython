#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from animal import Animal
from utils.util import log


class Dog(Animal):
    def __init__(self, name, color):
        super(Dog, self).__init__(name, color)

    # '@classmethod' could be another constructor
    @classmethod
    @log('static method')
    def age(cls, name, color, age):
        c = cls(name, color)
        c.age = age
        return c

    @classmethod
    def bark(cls):
        c = cls('dog', 'color')
        print('dog is barking...')
