from colorama import Fore, Style, init
init(autoreset=True)

class logger():
	@staticmethod
	def error(text, nline = False):
		if nline:
			print(Fore.RED + "\n[-] " + Fore.RESET + text)
		else:
			print(Fore.RED + "[-] " + Fore.RESET + text)

	@staticmethod
	def info(text, nline = False):
		if nline:
			print(Fore.BLUE + "\n[*] " + Fore.RESET + text)
		else:
			print(Fore.BLUE + "[*] " + Fore.RESET + text)

	@staticmethod
	def success(text, nline = False):
		if nline:
			print(Fore.GREEN + "\n[+] " + Fore.RESET + text)
		else:
			print(Fore.GREEN + "[+] " + Fore.RESET + text)

	@staticmethod
	def input(text):
		return input(Fore.MAGENTA + text + Fore.RESET)