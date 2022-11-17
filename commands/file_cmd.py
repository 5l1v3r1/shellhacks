from commands.command import Command
from logger import logger

class FileCmd(Command):
	def __init__(self, shellhacks):
		super().__init__("file", shellhacks)

	def run(self, arg):
		if len(arg) < 2:
			logger.info(f"Current file variable: {self.shellhacks.file if self.shellhacks.file != '' else 'None'}")
			return
		if len(arg) > 2:
			logger.error(f"Too many arguments for command '{self.name}'")
			return

		self.shellhacks.file = arg[1]
		self.shellhacks.storage.storage["file_var"] = self.shellhacks.file
		self.shellhacks.storage.save_storage()
		logger.success(f"File variable is now set to: {self.shellhacks.file}")