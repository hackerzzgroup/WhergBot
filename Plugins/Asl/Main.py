#!/usr/bin/env python
from random import choice
from .Settings import Settings

class Main(object):
	def __init__(self, Name, Parser):
		self.__name__ = Name
		self.Parser = Parser
		self.IRC = self.Parser.IRC

		self.genders = Settings.get('genders')
		self.agelist = Settings.get('ages')
		self.locations = Settings.get('locations')

	def Asl(self, data):
		self.IRC.say(data[2], "{0}/{1}/{2}".format(choice(self.agelist), choice(self.genders), choice(self.locations)))

	def Load(self):
		self.Parser.hookCommand('PRIVMSG', "(?:\s+?|^)asl(?:\s+?|$)", self.Asl)
		self.Parser.loadedPlugins[self.__name__].append(Settings)
		self.Parser.loadedPlugins[self.__name__].append(self.Load)
		self.Parser.loadedPlugins[self.__name__].append(self.Unload)
		self.Parser.loadedPlugins[self.__name__].append(self.Reload)

	def Unload(self):
		pass
	def Reload(self):
		pass
