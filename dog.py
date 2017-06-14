#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from animal import Animal


class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)

