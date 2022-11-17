from commands.command import Command
from logger import logger

class TargetCmd(Command):
	def __init__(self, shellhacks):
		super().__init__("target", shellhacks)

	def run(self, arg):
		if len(arg) < 2:
			logger.info(f"Current target variable: {self.shellhacks.target if self.shellhacks.target != '' else 'None'}")
			return
		if len(arg) > 2:
			logger.error(f"Too many arguments for command '{self.name}'")
			return

		self.shellhacks.target = arg[1]
		self.shellhacks.storage.storage["target_var"] = self.shellhacks.target
		self.shellhacks.storage.save_storage()
		logger.success(f"Target variable is now set to: {self.shellhacks.target}")