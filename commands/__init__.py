import json as JSON
from os import path
from logger import logger
from commands.clear_cmd import ClearCmd
from commands.exit_cmd import ExitCmd
from commands.target_cmd import TargetCmd
from commands.hash_cmd import HashCmd
from commands.file_cmd import FileCmd
from commands.url_cmd import UrlCmd
from commands.alias_cmd import AliasCmd
from commands.aliases_cmd import AliasesCmd

class Commands:
	def __init__(self, shellhacks):
		self.cmds = []
		self.shellhacks = shellhacks
		self.get_commands()

	def get_commands(self):
		self.cmds.append(ClearCmd(self.shellhacks))
		self.cmds.append(ExitCmd(self.shellhacks))
		self.cmds.append(TargetCmd(self.shellhacks))
		self.cmds.append(HashCmd(self.shellhacks))
		self.cmds.append(FileCmd(self.shellhacks))
		self.cmds.append(UrlCmd(self.shellhacks))
		self.cmds.append(AliasCmd(self.shellhacks))
		self.cmds.append(AliasesCmd(self.shellhacks))

	def run_script(self, sc, script_name):
		(desc, usage, cmd) = self.shellhacks.get_script_info(sc)
		usage = usage.split(" ")
		usage.pop(0)
		usage_str = ""
		for u in usage:
			usage_str+=u+(" " if usage.index(u)!=len(usage)-1 else "")

		if "[target]" in usage_str and self.shellhacks.target == "":
			logger.error(f"'{script_name.replace('.sh', '')}' needs a 'target'")
			return True

		if "[file]" in usage_str and self.shellhacks.target == "":
			logger.error(f"'{script_name.replace('.sh', '')}' needs a 'file'")
			return True

		if "[hash]" in usage_str and self.shellhacks.target == "":
			logger.error(f"'{script_name.replace('.sh', '')}' needs a 'hash'")
			return True

		if "[url]" in usage_str and self.shellhacks.target == "":
			logger.error(f"'{script_name.replace('.sh', '')}' needs a 'url'")
			return True
					
		usage_str = usage_str.replace("[target]", self.shellhacks.target)
		usage_str = usage_str.replace("[file]", self.shellhacks.file)
		usage_str = usage_str.replace("[hash]", self.shellhacks.hash)
		usage_str = usage_str.replace("[url]", self.shellhacks.url)
		self.shellhacks.run_script(sc, param=usage_str)
		return True

	def run_command(self, name):
		arg = name.split(" ")

		for cmd in self.cmds:
			if arg[0] == cmd.name:
				cmd.run(arg)
				return True

		for tool in self.shellhacks.tools:
			scripts = self.shellhacks.get_scripts(tool)
			for sc in scripts:
				script_name = sc.split("/")
				script_name = script_name[len(script_name)-1].replace(".sh", "")

				if (script_name+"_alias" in self.shellhacks.storage.storage.keys()):
					if arg[0] == self.shellhacks.storage.storage[script_name+"_alias"]:
						return self.run_script(sc, script_name)

				if arg[0] == script_name:
					return self.run_script(sc, script_name)


		return False