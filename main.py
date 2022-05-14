import os
import sys
from os.path import exists

from instagrapi import Client
from instagrapi.story import StoryBuilder, StoryMention
from instagrapi.types import Usertag, Location
from moviepy.video.VideoClip import VideoClip
from moviepy.video.fx.resize import resize
from moviepy.video.fx.accel_decel import accel_decel
from moviepy.video.fx.blackwhite import blackwhite
from moviepy.video.fx.blink import blink
from moviepy.video.fx.colorx import colorx
from moviepy.video.fx.crop import crop
from moviepy.video.fx.even_size import even_size
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
from moviepy.video.fx.freeze import freeze
from moviepy.video.fx.freeze_region import freeze_region
from moviepy.video.fx.gamma_corr import gamma_corr
from moviepy.video.fx.headblur import headblur
from moviepy.video.fx.invert_colors import invert_colors
from moviepy.video.fx.loop import loop
from moviepy.video.fx.lum_contrast import lum_contrast
from moviepy.video.fx.make_loopable import make_loopable
from moviepy.video.fx.margin import margin
from moviepy.video.fx.mask_and import mask_and
from moviepy.video.fx.mask_color import mask_color
from moviepy.video.fx.mask_or import mask_or
from moviepy.video.fx.mirror_x import mirror_x
from moviepy.video.fx.mirror_y import mirror_y
from moviepy.video.fx.painting import painting
from moviepy.video.fx.resize import resize
from moviepy.video.fx.rotate import rotate
from moviepy.video.fx.scroll import scroll
from moviepy.video.fx.speedx import speedx
from moviepy.video.fx.supersample import supersample
from moviepy.video.fx.time_mirror import time_mirror
from moviepy.video.fx.time_symmetrize import time_symmetrize
from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from moviepy.audio.fx.audio_left_right import audio_left_right
from moviepy.audio.fx.audio_loop import audio_loop
from moviepy.audio.fx.audio_normalize import audio_normalize
from moviepy.audio.fx.volumex import volumex

VideoClip.resize = resize

# from moviepy.editor import TextClip
# print(TextClip.list("font"))


cl = Client()
user = "bf_bruteforce"  # ID for Insta
passw = "Brute.5.Force"  # Pass
wuser = os.getlogin()
dirName = f"/Users/{wuser}/Videos/AutoInstaStory"  # The directory to check
mentions = dirName + "/mentions.txt"  # mentions path
storyFolder = dirName + "/Story"
clipFolder = dirName + "/Clip"
user_mentions = []

if os.path.exists(dirName) is False:
    os.mkdir(dirName)  # Main Directory
    print(f"\nNo Directory Found\nDirectory Created: \"{dirName}\"\n\n")

if exists(mentions) is False:
    print("Mentions File not find making new one\n\n")
    with open(mentions, 'w') as f:
        f.write('i__m.ahmad')
        f.close()

if os.path.exists(storyFolder) is False:
    os.mkdir(storyFolder)  # Story Folder

if os.path.exists(clipFolder) is False:
    os.mkdir(clipFolder)  # Clip Folder

backgrpath = f"/Users/{wuser}/AppData/Roaming/AutoInstaStory/background.jpg"  # background path
font = 'Segoe-Print'

megaCaption = "\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n #valorant #twitch #gaming #gamer #valorantclips" \
              " #fortnite #csgo #valorantgame #leagueoflegends #riotgames #valorantgameplay #streamer " \
              " #esports #lol #valorantmemes #twitchstreamer #game #pubg #pcgaming #pc #valoranthighlight" \
              " #youtube #rkiye #ps #memes #PulsarFuture #games #riot #callofduty #valorantnews #apexlegends "

try:
    mem = f'/Users/{wuser}/AppData/Roaming/AutoInstaStory'

    if os.path.exists(mem) is False:
        os.mkdir(mem)

    if os.path.exists(backgrpath) is False:
        print("No Background found for Story\n\n")
        backgrpath = ""

    if exists(mentions) is False:
        print("Mentions File not find making new one\n\n")
        with open(mentions, 'w') as f:
            f.write('i__m.ahmad')
            f.close()

    if exists(f'/Users/{wuser}/AppData/Roaming/AutoInstaStory/session.json'):
        cl.load_settings(f'/Users/{wuser}/AppData/Roaming/AutoInstaStory/session.json')

    cl.login(user, passw)

except Exception as e:
    print("An error was encountered while logging in\n", str(e))
    os.system('pause')
    sys.exit()

else:
    print("\n \nSuccessfully logged in Instagram! ---- USERNAME = ", user)
    cl.dump_settings(f'/Users/{wuser}/AppData/Roaming/AutoInstaStory/session.json')
    try:
        f = open(mentions, "r")

        while True:
            mention = f.readline()
            if not mention:
                break
            user_mentions.append(cl.user_info_by_username(mention.rstrip()))

    except Exception as e:
        print("Error Fetching IDs\n", str(e))
        os.system('pause')
        sys.exit()

    else:
        print("\nIDs fetched successfully!")


def dircheck(folder):
    if len(os.listdir(folder)) != 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(" \n \n"
          "***************************************************************\n*\n"
          "*             Welcome to Instagram Auto Uploader! \n"
          "*                   *** Made by Avcton *** \n*\n"
          "*  Upload your desired content in the following folder:\n"
          "*         ", dirName,
          "\n*\n*   Use '%' in the file name for caption (Story or Clip) \n"
          "*  You can add mentions line by line in the mentions.txt file\n* ",
          "\n***************************************************************\n\n")

    ifile = None
    caption = ""
    vanish = False
    story = os.listdir(storyFolder)
    clip = os.listdir(clipFolder)
    print("A total of", len(story), "file(s) were found for story uploading \n")
    print("A total of", len(clip), "file(s) were found for clip uploading \n")

    if dircheck(storyFolder):
        vanish = True
        for file in story:
            caption = ""
            users = []
            ifile = file
            path = storyFolder + '/' + file

            if file.find("%") != -1 and (path.endswith('.mp4') or path.endswith('.png') or path.endswith('.jpg')):
                print("\n \nStory = ", file)
                caption = input("Enter a caption for the story: ")

            for user in user_mentions:
                users.append(StoryMention(user=user, x=0.49892962))

            if path.endswith('.mp4'):
                try:
                    buildout = StoryBuilder(
                        path=path,
                        caption=caption,
                        mentions=users,
                        bgpath=backgrpath
                    ).video(max_duration=40, font=font)

                    cl.video_upload_to_story(buildout.path, mentions=buildout.mentions)

                except Exception as e:
                    print("\n\n An error was encountered for file: ", file, "\n", str(e))
                    os.system('pause')
                    sys.exit()
                else:
                    print("\n \n", file, " ", "Story uploaded successfully!")

            elif path.endswith('.png') or path.endswith('.jpg') or path.endswith('.jpeg'):
                try:
                    buildout = StoryBuilder(path, caption, users, backgrpath).photo(
                        max_duration=6, font=font)

                    cl.video_upload_to_story(buildout.path, mentions=buildout.mentions)
                except Exception as e:
                    print("\n\n An error was encountered for file: ", file, "\n", str(e))
                    os.system('pause')
                    sys.exit()
                else:
                    print("\n \n", file, " ", "Story uploaded successfully!")

            else:
                print(f'Invalid file: {file} \nIgnoring File..\n')

    if dircheck(clipFolder):
        vanish = True
        for file in clip:
            caption = ""
            users = []
            ifile = file
            path = clipFolder + '/' + file

            for user in user_mentions:
                users.append(Usertag(user=user, x=0.5, y=0.5))

            if file.find("%") != -1 and (path.endswith('.mp4') or path.endswith('.png') or path.endswith('.jpg')):
                print("\n \nClip = ", file)
                caption = input("Enter a caption for the clip: ")

            caption = caption + megaCaption

            if path.endswith('.mp4'):
                try:
                    cl.video_upload(path=path, caption=caption, usertags=users,
                                    location=Location(name='Somewhere in Valorant'))

                except Exception as e:
                    print("\n\n An error was encountered for file: ", file, "\n", str(e))
                    os.system('pause')

                else:
                    print("\n \n", file, " ", "Post uploaded successfully!")

            elif path.endswith('.png') or path.endswith('.jpg') or path.endswith('.jpeg'):
                try:
                    cl.photo_upload(path=path, caption=caption, usertags=users)

                except Exception as e:
                    print("\n\n An error was encountered for file: ", file, "\n", str(e))
                    os.system('pause')
                    sys.exit()

                else:
                    print("\n \n", file, " ", "Post uploaded successfully!")

            else:
                print(f'Invalid file: {file} \nIgnoring File..\n')

    if not vanish:
        os.system('pause')
