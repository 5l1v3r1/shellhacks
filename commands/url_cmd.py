from commands.command import Command
from logger import logger

class UrlCmd(Command):
	def __init__(self, shellhacks):
		super().__init__("url", shellhacks)

	def run(self, arg):
		if len(arg) < 2:
			logger.info(f"Current URL variable: {self.shellhacks.url if self.shellhacks.url != '' else 'None'}")
			return
		if len(arg) > 2:
			logger.error(f"Too many arguments for command '{self.name}'")
			return

		self.shellhacks.url = arg[1]
		self.shellhacks.storage.storage["url_var"] = self.shellhacks.url
		self.shellhacks.storage.save_storage()
		logger.success(f"URL variable is now set to: {self.shellhacks.url}")