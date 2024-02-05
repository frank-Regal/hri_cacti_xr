#/usr/bin/python3

import argparse
import gdown
from gdown.exceptions import FolderContentsMaximumLimitError

# map of directory names in google drive with their assosciated shared link
dir_map_ = {
	"stop": "https://drive.google.com/drive/folders/1At6ziRX_1YmhQ-P5iQeDEvJjZG_6pCk6",
	"hold": "https://drive.google.com/drive/folders/14vQpGBBHmJ1QLEV7eIUX8eAWZ9PZI3VZ",
	"go_right": "https://drive.google.com/drive/folders/1NAqsTA78FcKx43upJtdcGu0IyEvpNj0Q"
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
        for input_dir in args.dir:
            if(dir_map_.get(input_dir) == None):
                print(f"'{input_dir}' directory does not exist in map [see line 8]")
            for dir_name, url in dir_map_.items():
                if (input_dir == dir_name):
                    print("Downloading data from \"" + dir_name + "\" directory.")
                    try:
                        gdown.download_folder(url, quiet=False, use_cookies=False)
                    except FolderContentsMaximumLimitError:
                        print("no good")


    # download data from all folders
    else:
        user_response = input("Are you sure you want to download all folders? [Y/n] ")
        if (user_response == "Y" or user_response == "y"):
            for dir_name, url in dir_map_.items():
                print("Downloading data from \"all\" folders. This may take a while ...")
                gdown.download_folder(url, quiet=False, use_cookies=False)
        else:
            print("Done.")

if __name__ == "__main__":
    main()
