from os import path
import json as JSON

class Storage:
	def __init__(self):
		self.path = path.abspath(path.join("storage", "storage.json"))
		self.storage = self.get_storage()

	def get_storage(self):
		if not path.exists(self.path) or not path.isfile(self.path):
			f = open(self.path, "w")
			json = {
				"target_var": "",
				"url_var": "",
				"file_var": "",
				"hash_var": ""
			}
			f.write(JSON.dumps(json))
			f.close()
		else:
			f = open(self.path, "r")
			json = JSON.loads(f.read())
			f.close()

		return json

	def save_storage(self):
		with open(self.path, "w") as f:
			f.write(JSON.dumps(self.storage))
			f.close()