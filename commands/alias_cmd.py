from commands.command import Command
from logger import logger
import string

class AliasCmd(Command):
	def __init__(self, shellhacks):
		super().__init__("alias", shellhacks)

	def run(self, arg):
		if len(arg) > 3:
			logger.error(f"Too many arguments for command '{self.name}'")
			return
		if len(arg) < 3:
			logger.error(f"'{self.name}' needs 2 arguments: 'script' and 'alias'")
			return

		script = arg[1]
		alias = arg[2]
		for char in alias:
			if not (char in list(string.ascii_letters)+list(string.digits)+["_", "."]):
				logger.error("Aliases can only contain letters, digits, dots and underscores")
				return
		for char in script:
			if not (char in list(string.ascii_letters)+list(string.digits)+["_"]):
				logger.error("Unvalid script")
				return

		self.shellhacks.storage.storage[script+"_alias"] = alias
		logger.info("Saving the alias...")
		self.shellhacks.storage.save_storage()

		logger.success("Alias successfully saved")