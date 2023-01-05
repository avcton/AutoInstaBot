# AutoInstaBot
> An autobot script made in python using the [instagrapi](https://github.com/adw0rd/instagrapi) library.

It uses the local folder structure to grab multiple files as input. The instagram credentials should be hardcoded into the script.

The Login Session is generated on first run for the device and used for futher runs. 

Currently it supports clip and story uploading.

The clips will be taken from your `/User/Videos/Clip` folder and for the stories it will be `Videos/Story`.

A `mentions.txt` file can be used to mention users in story or clips accordingly. New mentions on new lines.

A background can be used for story uploading. The path for this background file would be `/User/AppData/Roaming/AutoInstaStory/background.jpg`

If `%` is found in the file name then that file's name is used as a caption for both story and clip.

Current files supported: `.mp4` for videos and `.png .jpg .jpeg` for images.
