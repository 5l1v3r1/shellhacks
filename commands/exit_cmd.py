from commands.command import Command
from logger import logger

class ExitCmd(Command):
	def __init__(self, shellhacks):
		super().__init__("exit", shellhacks)

	def run(self, arg):
		if len(arg) != 1:
			logger.error(f"Too many arguments for command '{self.name}'")
			return

		logger.info("Bye!")
		exit()
