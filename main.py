from __future__ import unicode_literals
import pytube

def download_one_music(url):
    try:
        yt = pytube.YouTube(url)
    except: #KEEP THAT SHIT SIMPLE ( one exception catch all )
         print(f'Video on url {url} is unavaialable, skipping.')
    else: 
        print(f'Downloading video: {url}')
        yt.streams.filter(only_audio=True).get_by_itag(140).download(output_path="./output", filename=yt.title+".mp3")
        
with open("./musicList.txt") as file:
    for line in file:
        line = line.strip()
        download_one_music(line)

