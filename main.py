import metadata

def main():
	print("Read values for IMG_0613.mp4")
	file = "./IMG_0613.mp4"
	md = metadata.MetaData(file)

	# Print metadata values
	print("codecs: ", md.get_codecs())
	print("height: ", md.get_height())
	print("width: ", md.get_width())
	print("fps: ", md.get_fps())


	print("Read values for IMG_0753.MOV")
	file = "./IMG_0753.MOV"
	md = metadata.MetaData(file)

	# Print metadata values
	print("codecs: ", md.get_codecs())
	print("height: ", md.get_height())
	print("width: ", md.get_width())
	print("fps: ", md.get_fps())

if __name__ == '__main__':
	main()
