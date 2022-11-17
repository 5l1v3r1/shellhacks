from commands.command import Command
from os import system
from logger import logger

class ClearCmd(Command):
	def __init__(self, shellhacks):
		super().__init__("clear", shellhacks)

	def run(self, arg):
		if len(arg) != 1:
			logger.error(f"Too many arguments for command '{self.name}'")
			return

		system("clear")
