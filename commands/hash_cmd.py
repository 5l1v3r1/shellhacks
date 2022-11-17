from commands.command import Command
from logger import logger

class HashCmd(Command):
	def __init__(self, shellhacks):
		super().__init__("hash", shellhacks)

	def run(self, arg):
		if len(arg) < 2:
			logger.info(f"Current hash variable: {self.shellhacks.hash if self.shellhacks.hash != '' else 'None'}")
			return
		if len(arg) > 2:
			logger.error(f"Too many arguments for command '{self.name}'")
			return

		self.shellhacks.hash = arg[1]
		self.shellhacks.storage.storage["hash_var"] = self.shellhacks.hash
		self.shellhacks.storage.save_storage()
		logger.success(f"Hash variable is now set to: {self.shellhacks.hash}")