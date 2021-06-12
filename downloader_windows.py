import youtube_dl

action = ""
options = ""
while action != "quit":
	action = input("Enter URL to download or 'quit' to quit: ")
	options = ""
	if action != "quit":
		while not options in ["A", "a", "V", "v", "quit"]:
			options = input("Audio/video? [A/v] 'quit' to quit: ")
			if options == "A" or options == "a":
				ytdl_opts = {"ffmpeg_location":"ffmpeg-4.4-essentials_build/bin/ffmpeg.exe", "format":"bestaudio/best",
				 "postprocessors": [{
					"key": "FFmpegExtractAudio",
					"preferredcodec": "mp3"
					}]}
				ytdl = youtube_dl.YoutubeDL(ytdl_opts)
				try:
					with ytdl as yt:
						yt.download([action])
					break
				except Exception:
					break
			elif options == "V" or options == "v":
				ytdl_opts = {"ffmpeg_location":"ffmpeg-4.4-essentials_build/bin/ffmpeg.exe",
				 "postprocessors": [{
					"key": "FFmpegVideoConvertor",
					"preferedformat": "mp4"
					}]}
				ytdl = youtube_dl.YoutubeDL(ytdl_opts)
				try:
					with ytdl as yt:
						yt.download([action])
					break
				except Exception:
					break
			else:
				if options != "quit":
					print("Invalid option!")
