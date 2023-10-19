from pytube import YouTube
import os
from moviepy.editor import VideoFileClip

arquivo_links = "list.txt"
out = "./out/"

if not os.path.exists(out):
    os.makedirs(out)

def baixar_musicas(links):
    for link in links:
        try:
            yt = YouTube(link)
            video_path = yt.streams.filter(only_audio=False).first().download(output_path=out)
            mp4_filename = os.path.basename(video_path)
            
            mp3_filename = os.path.splitext(mp4_filename)[0] + ".mp3"
            mp4_path = os.path.join(out, mp4_filename)
            mp3_path = os.path.join(out, mp3_filename)
            
            # Converter o arquivo MP4 para MP3
            video = VideoFileClip(mp4_path)
            audio = video.audio
            audio.write_audiofile(mp3_path)
            
            # Remover o arquivo MP4, se desejar
            os.remove(mp4_path)
            
            print(f"{yt.title} baixada e convertida com sucesso para MP3!")
        except Exception as e:
            print(f"Erro ao baixar {link}: {str(e)}")

def ler_links_de_arquivo(arquivo):
    links = []
    with open(arquivo, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("http"):
                links.append(line)
    return links

links = ler_links_de_arquivo(arquivo_links)

baixar_musicas(links)
