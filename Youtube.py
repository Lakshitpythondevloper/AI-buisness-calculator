import yt_dlp


class Youtube:

    def __init__(self):
        self.a = "Hello! Welcome to AI_buisness calaculator! 😉"
        print(self.a)

    def download_video(self, url):
        
        youtube_url = url
        self.youtube_video = yt_dlp.YoutubeDL()
        self.youtube_video.download(youtube_url)

    def download_audio(self,url):

        youtube_url = url
        youtube_audio = yt_dlp.YoutubeDL({'format': 'bestaudio'})
        youtube_audio.download(youtube_url)