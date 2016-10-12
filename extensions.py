import os, sys
from PIL import Image

class Files(object):

	def __init__(self, path):
		self.path = path
		os.chdir(self.path)
		self.files = [ f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f)) ]
		self.not_pictures = []
		self.files_removed = 0
		self.files_changed = 0

	def list_files(self):
		for f in enumerate(self.files):
			print(f)

	def check_format(self, fname):
		try:
			with Image.open(fname) as image:
				format = image.format
				return format
		except:
			self.not_pictures.append(fname)
			print(fname + ": Not a picture file format")
			return 0

	def remove_picture_less_than(self, fname, size=1920*1080):
		with Image.open(fname) as image:
			width, height = image.size
			if width*height < size:
				image.close()
				os.remove(fname)
				self.files_removed += 1
				return True
		return 0

	def change_ext(self, fname, file_ext, format):
		if file_ext == "":
			new_file_name = fname + "." + format
			os.renames(os.path.join(self.path, fname), os.path.join(self.path, new_file_name))
			self.files_changed += 1
			return True
		return False

	def print_changes(self):
		print("Number of files deleted: %s"  %self.files_removed)
		print("Number of files changed: %s"  %self.files_changed)

	def change_all(self):
		for f in self.files:
			file_name, file_ext = os.path.splitext(f)
			format = self.check_format(f)
			if format != 0:
				if self.remove_picture_less_than(f):
					continue
				self.change_ext(f, file_ext, format)

		for f in self.not_pictures:
			os.remove(f)
			self.files_removed += 1
