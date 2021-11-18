"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class Weapon:
	def __init__(self, name, power, minlevel):
		self.__name = name
		self.power = power
		self.minlevel = minlevel

	@property
	def name(self):
		return self.__name

	def make_unarmed(self):
		self.__name = "Unarmed"
		self.power = 20


class Character:
	def __init__(self, name, max_hp, attack, defense, level, weapon, hp):
		self.name = name
		self.max_hp = max_hp
		self.attack = attack
		self.defense = defense
		self.level = level
		self.weapon = weapon
		self.hp = hp

	def compute_damage(self, a, d):
		self.attacker = a
		self.defender = d

		if random.random() < (1/16):
			crit = 2
		else:
			crit = 1

		self.damage = int(((((((2 * a.level)/5) + 2) * a.weapon.power * (a.attack/d.defense))+ 2)/50) * (crit * random.uniform(0.85, 1.00)))

		return self.damage

	#@name.setter
		#def name(self, value):
			#self.__name = value

def deal_damage(attacker, defender):
	# TODO: Calculer dégâts
	pass


def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	pass
