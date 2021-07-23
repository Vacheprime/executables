#! /usr/bin/env python3 
import youtube_dl
import os
import lib_programname
filename = os.path.basename(__file__)
path = lib_programname.get_path_executed_script()
path = str(path).replace(filename, "")
print(f"Executable path: {path}")
def download_audio(url, codec="mp3"):
	global path
	"""
	codec : audio codec chosen to download/convert. Default is mp3
	url : url specified
	"""
	
	ytdl_opts = {"ffmpeg_location":f"{path}ffmpeg-git-20210528-amd64-static/ffmpeg", "format":"bestaudio/best",
	"postprocessors": [{"key": "FFmpegExtractAudio","preferredcodec": codec}]}
	ytdl = youtube_dl.YoutubeDL(ytdl_opts)
	try:
		with ytdl as yt:
			yt.download([url])
	except KeyError as e:
		print(f"Invalid format: {e}")


def download_video(url, video_format="mp4"):
	global path
	"""
	video_format : video format chosen to download/convert. Default is mp4
	url : url specified
	"""
	
	ytdl_opts = {"ffmpeg_location":f"{path}ffmpeg-git-20210528-amd64-static/ffmpeg",
	"postprocessors": [{"key": "FFmpegVideoConvertor","preferedformat": video_format}]}
	ytdl = youtube_dl.YoutubeDL(ytdl_opts)
	try:
		with ytdl as yt:
			yt.download([url])
	except KeyError as e:
		print(f"Invalid format: {e}")
				
url = ""
options = ""
audio_options = ""
video_options = ""
while url != "quit":
	url = input("Enter URL to download or 'quit' to quit: ")
	options = ""
	if url != "quit":
		while not options in ["A", "a", "V", "v", "quit"]:
			options = input("Audio/video? [A/v] 'quit' to quit: ")
			if options == "A" or options == "a":
				audio_options = input("Enter desired audio format (default is mp3): ")
				if audio_options == "":
					download_audio(url)
				else:
					download_audio(url, audio_options)
					
			elif options == "V" or options == "v":
				video_options = input("Enter desired video format (default is mp4): ")
				if video_options == "":
					download_video(url)
				else:
					download_video(url, video_options)
					
			else:
				if options != "quit":
					print("Invalid option!")
