from os import path
from os import listdir
from os import system
import platform
import readline
from prettytable import PrettyTable

from logger import logger
from commands import Commands
from storage import Storage

class Shellhacks:
	def __init__(self):
		self.version = "0.1"
		self.logger = logger()
		self.storage = Storage()
		self.commands = Commands(self)
		
		self.target = self.storage.storage["target_var"]
		self.file = self.storage.storage["file_var"]
		self.hash = self.storage.storage["hash_var"]
		self.url = self.storage.storage["url_var"]

		if not self.sys_check():
			self.logger.error("Shellhacks only supports linux based operating systems.")

		self.logger.success(f"Started up shellhacks {self.version}")

		self.scripts_base_dir = path.abspath("scripts")
		self.tools = listdir(self.scripts_base_dir)
		self.tool_dirs = []
		for tool in self.tools:
			self.tool_dirs.append(path.join(self.scripts_base_dir, tool))

	def sys_check(self):
		if (platform.system() == "Linux" or platform.system() == "Darwin"):
			return True
		else:
			return False

	def get_scripts(self, tool):
		for tool_dir in self.tool_dirs:
			if tool == tool_dir.split("/").pop():
				scripts = []
				for script in listdir(tool_dir):
					scripts.append(path.join(tool_dir, script))
				return scripts

		return None

	def get_script_info(self, script):
		f = open(script, "r")
		content = f.read()
		f.close()

		second_line = content.split("\n")[1]
		if not second_line.startswith("#DESC:"):
			desc = "None"
		desc = second_line.split(":")[1]

		third_line = content.split("\n")[2]
		if not third_line.startswith("#USAGE:"):
			third_line = "None"
		usage = third_line.split(":")[1]

		fourth_line = content.split("\n")[3]
		if not fourth_line.startswith("#CMD:"):
			fourth_line = "None"
		cmd = fourth_line.split(":")[1]

		return (desc, usage, cmd)

	def run_script(self, script, param=None):
		with open(script, "r") as f:
			content = f.read()
			if not content.startswith("#SHTRUST"):
				self.logger.error(f"Contents of {script} seems to be changed, something malicious maybe going on!")
				return
		system(f"sh {script} {param if param!=None else ''}")

	def run_cmd(self, name):
		result = self.commands.run_command(name)
		if not result:
			name_list = name.split(" ")
			if len(name_list) == 1:
				tool_name = name_list[0]
				if not tool_name in self.tools:
					self.logger.error(f"No command/script/alias named '{name}'")
					return
				self.logger.info(f"Listing scripts for '{tool_name}'")
				tool_scripts = self.get_scripts(tool_name)
				scripts_table = PrettyTable(["Name", "Description", "Usage", "Command"])
				for script in tool_scripts:
					
					(desc, usage, cmd) = self.get_script_info(script)

					scripts_table.add_row([script.split("/").pop().split(".")[0], desc, usage, cmd])
				print(scripts_table)
			else:
				self.logger.error(f"No command/script/alias named '{name_list[0]}'")	


if __name__ == "__main__":
	shellhacks = Shellhacks()
	while True:
		try:
			cmd = shellhacks.logger.input("-> ")
		except:
			shellhacks.logger.info("Bye!", nline=True)
			exit()
		if cmd != "":
			shellhacks.run_cmd(cmd)

