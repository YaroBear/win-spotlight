#Windows Spotlight Pictures
Do you likes those Windows 10 lockscreen backgrounds? Have you wanted a nice and easy way to get to all of them? Me too. That's why I made this little script.

The spotlight pictures folder contains landscape photos (1920x1080) and mobile/vertical photos (1080x1920), random thumbnails for other things, and some unknown files. All of them don't have any extensions.

So this scripts takes the unmarked files, adds the proper extensions, and discards all the other random thumbnails and unkown files. So all you're left with is beautiful landscape and vertical photos.

##Getting Started
All you got to do is set the source folder, and destination folder in main.py
```python
def main():
	win_spotlight_dir = "C:/Users/<name>/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets"
	dest_dir = "C:/Users/<name>/Desktop/spotlight"
```
It will create the destination directory for you if it doesn't already exist.

It copies one directory to the other, and then makes changes in the destination directory. So don't worry about it messing up the original folder.