import random
import time
import os
import platform

class Game:
	def intro(self):
		print('=' * 20)
		print('    Memory Game')
		print('=' * 20)
		print('\n')

	def roll(self):
		if self.difficulty.lower() == 'e':
			self.number = random.randint(100, 1000)
		elif self.difficulty.lower() == 'm':
			self.number = random.randint(10000, 100000)
		elif self.difficulty.lower() == 'h':
			self.number = random.randint(100000, 1000000)
		print('#' * 10)
		print('-' * 10)
		print(self.number)
		print('-' * 10)
		print('#' * 10)
	def choose(self):
		try:
			self.choice = int(input('What is the number? '))
		except ValueError:
			print('Invalid selection: Type a number')
			self.choose()

	def __init__(self):
		self.score = 0
		self.intro()
		while True:
			self.difficulty = input('Select a difficulty: [e]asy, [m]edium, [h]ard: ')
			os.system('pause')
			print('\n')
			self.roll()
			if platform.system() == 'Windows':
				time.sleep(0.03)
				os.system('cls')
			elif platform.system() == 'Linux':
				os.system('sleep 0.03')
				os.system('clear')
			self.choose()
			try:
				if int(self.choice) == self.number:
					print('Correct!')
					self.score += 1
					print('Your score is now {}.'.format(self.score))
					print('\n')
				else:
					print('Incorrect!')
					self.score -= 1
					print('Your score is now {}.'.format(self.score))
			except ValueError:
				continue

Game()
