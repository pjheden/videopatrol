import os # run os commands
import subprocess # capture os output


class MetaData:
	def __init__(self, file):
		self.file = file
		# Read codecs
		cmd = 'mdls -name kMDItemCodecs ' + file
		result = self.run_cmd(cmd)
		self.codecs = result

		# Read height
		cmd = 'mdls -name kMDItemPixelHeight ' + file
		result = self.run_cmd(cmd)
		self.height = result

		# Read width
		cmd = 'mdls -name kMDItemPixelWidth ' + file
		result = self.run_cmd(cmd)
		self.width = result


		# Get FPS
		import cv2
		cap=cv2.VideoCapture(file)
		self.fps = cap.get(cv2.CAP_PROP_FPS)

	def run_cmd(self, cmd_str):
		res = subprocess.run([cmd_str], shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
		return res.split(" = ")[1]

	def get_codecs(self):
		return self.codecs

	def get_height(self):
		return self.height

	def get_width(self):
		return self.width

	def get_fps(self):
		return self.fps
