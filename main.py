from pytube import YouTube
from pytube import Playlist
from moviepy.editor import *
import os

print('''
 __   __            _____        _             ____   _                _  _       _   
 \ \ / /___   _   _|_   _|_   _ | |__    ___  |  _ \ | |  __ _  _   _ | |(_) ___ | |_ 
  \ V // _ \ | | | | | | | | | || '_ \  / _ \ | |_) || | / _` || | | || || |/ __|| __|
   | || (_) || |_| | | | | |_| || |_) ||  __/ |  __/ | || (_| || |_| || || |\__ \| |_ 
   |_| \___/  \__,_| |_|  \__,_||_.__/  \___| |_|    |_| \__,_| \__, ||_||_||___/ \__|
         ____                          _                    _   |___/                 
        |  _ \   ___ __      __ _ __  | |  ___    __ _   __| |  ___  _ __            
        | | | | / _ \\ \ /\ / /| '_ \ | | / _ \  / _` | / _` | / _ \| '__|           
        | |_| || (_) |\ V  V / | | | || || (_) || (_| || (_| ||  __/| |              
        |____/  \___/  \_/\_/  |_| |_||_| \___/  \__,_| \__,_| \___||_|              
                                                                                      

''')

if not os.path.isdir('temp'):
    os.mkdir('temp')

if not os.path.isdir('converted'):
    os.mkdir('converted')

playlist = Playlist(input('Just a reminder that this will download ALL videos in the playlist\nPaste a YouTube Playlist here: '))
dest = str(os.getcwd()) + '\\temp'

def main():

    for vid in playlist.video_urls:
        video = YouTube(vid)
        title = video.title

        if '/' or '\\' in title:
            title = title.replace('/', '')
            title = title.replace('\\', '')
        try:
            a = video.streams.get_by_itag(18).download(output_path=dest)
            print('Video Downloaded...')
            downloaded_video = VideoFileClip(a)
        except Exception as e:
            print(f'Exception occurred: {e}')
            with open('missing_songs.txt', 'a') as f:
                f.append(vid + '\n')
                        
        try:
            audio_from_video = downloaded_video.audio
            audio_from_video.write_audiofile('converted\\'+" ".join(title.split())+'.mp3')

        except Exception as e:
            print(f'Exception occurred: {e}')

        audio_from_video.close()
        downloaded_video.close()

    out = os.listdir('temp')
    filepath = os.getcwd()

    for file in out:
        os.remove(filepath +'//temp//'+ file)


if __name__ == '__main__':
    main()

