from extensions import Files
from distutils.dir_util import copy_tree
import os

def main():
	win_spotlight_dir = "C:/Users/yaro/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets"
	dest_dir = "C:/Users/yaro/Desktop/spotlight"

	copy_tree(win_spotlight_dir, dest_dir)

	folder = Files(dest_dir)
	folder.change_all()
	folder.print_changes()


if __name__ == '__main__':
	main()
