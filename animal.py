#!/usr/bin/env python3
# -*- coding=utf-8 -*-


class Animal(object):
	def __init__(self, name, color):
		self.__name = name
		self.__color = color

	# self.__class__.__name__ 获取当前类的名字
	# __str__
	def __str__(self):
		return '%s object (name: %s)' % (self.__class__.__name__, self.__name)

	__repr__ = __str__

	# 用于限制当前类实例的动态添加属性
	__slots__ = ('__name', '__color')

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name

	def get_color(self):
		return self.__color

	def set_color(self, color):
		self.__color = color

	def run(self):
		if not isinstance(self.get_name(), str) or not self.get_name():
			print('Animal is running...')
		else:
			print('%s is running...' % self.get_name())

	# if not self.get_name(): check string is empty or whitespace
	def introduce(self):
		if (not isinstance(self.get_name(), str) or not self.get_name()) \
				and (not isinstance(self.get_color(), str) or not self.get_color()):
			print('It\'s an %s!!!' % self.__class__.__name__)
		elif not isinstance(self.get_name(), str) or not self.get_name():
			print('It\'s %s %s!!!' % (self.get_color(), self.__class__.__name__))
		elif not isinstance(self.get_color(), str) or not self.get_color():
			print('%s is an %s!!!' % (self.get_name(), self.__class__.__name__))
		else:
			print('%s is %s %s!!!' % (self.get_name(), self.get_color(), self.__class__.__name__))
