#/usr/bin/python3

import argparse
import gdown
from gdown.exceptions import FolderContentsMaximumLimitError

# map of directory names in google drive with their assosciated shared link
dir_map_ = {
	"stop": "https://drive.google.com/drive/folders/1At6ziRX_1YmhQ-P5iQeDEvJjZG_6pCk6"
}

def main():
    
	# create a parser object
	parser = argparse.ArgumentParser()

	# add arguments
	parser.add_argument('-d', '--dir', nargs='+', help='Name of directories from gdrive you would like to download.')
	
	# parse arguments
	args = parser.parse_args()

	# download data from specified folders
	if args.dir:
		for dir_name, url in dir_map_.items():
			for input_dir in args.dir:
				if (input_dir == dir_name):
					print("Downloading data from \"" + dir_name + "\" directory.")
					try:
						gdown.download_folder(url, quiet=False, use_cookies=False)
					except FolderContentsMaximumLimitError:
						print("ERROR: There are 50 or more files in the directory! Split them up into seperate directories.")

	# download data from all folders
	else:
		user_response = input("Are you sure you want to download all folders? [Y/n] ")
		if (user_response == "Y" or user_response == "y"):
			for dir_name, url in dir_map_.items():
				print("Downloading data from \"all\" folders. This may take a while ...")
				try:
					gdown.download_folder(url, quiet=False, use_cookies=False)
				except FolderContentsMaximumLimitError:
					print("ERROR: There are 50 or more files in the directory! Split them up into seperate directories.")
		else:
			print("Done.")

if __name__ == "__main__":
	main()
