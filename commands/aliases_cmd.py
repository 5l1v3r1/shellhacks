from commands.command import Command
from logger import logger
from prettytable import PrettyTable

class AliasesCmd(Command):
	def __init__(self, shellhacks):
		super().__init__("aliases", shellhacks)

	def run(self, arg):
		if len(arg) != 1:
			logger.error(f"Too many arguments for command '{self.name}'")
			return

		logger.info("Listing aliases...")

		alias_table = PrettyTable(["Alias", "Command"])
		for key in self.shellhacks.storage.storage.keys():
			if key.endswith("_alias"):
				alias_table.add_row([self.shellhacks.storage.storage[key], key.replace("_alias", "")])
				
		print(alias_table)