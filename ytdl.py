from pytube import YouTube, Playlist
import os

def download_song(song_link, dest):
	''' 
	Downloads an mp3 audio stream and save it to a destination. 
	'''

	# change to get the highest quality audio stream, but for now default to 140
	song = YouTube(song_link)
	audio_stream = song.streams.get_by_itag(140)
	audio_stream.download(output_path=dest, filename=song.title+'.mp3')

	# i was hesitant about making this return the song name, but I needed it for download_songs_from_playlist
	return song.title

def download_songs_from_playlist(playlist_link, dest):
	'''
	Downloads all videos in a playlist as mp3 files to a destination.
	'''
	try:
		songs = Playlist(playlist_link)
	except Exception as e:
		print(e)
		print('Invalid playlist link.')
		input('Press any key to exit...')
		exit()

	# add threads here to download more at once.
	song_names = []

	for song in songs:
		try:
			name = download_song(song, dest)
			song_names.append(name)
			print(f'Downloading {song}')
		except:
			print(f'Error downloading {song}, skipping...')
			continue

	print(f'Downloaded {len(song_names)} audios successfully!')
	print(song_names)

def main():
	# if no output folder exists, we create it

	link = input('Input a YouTube video/playlist link: ')
	input_dest = input('Destination folder (none for current directory): ')
	dest = ''
	run_again = False

	# if the user gives an output dir, we create it, otherwise we default to output in the current dir
	if input_dest:
		dest = input_dest

		if not os.path.isdir(input_dest):
			try:
				os.mkdir(input_dest)
			except Exception as e:
				print(e)
				print('There was an error creating that destination. Try again.')
				input('Press any key to exit...')
				exit()
	else:
		dest = os.getcwd()+'/output'

		if not os.path.isdir('output'):
			os.mkdir('output')

	# check if its a video or playlist
	if ('https://' and 'playlist') in link:	
		download_songs_from_playlist(link, dest)
		run_again = input('Download another? y/n: ')
	elif ('https://' and ('watch' or 'https://youtu.be')) in link:
		try:
			name = download_song(link, dest)
			print(f'Downloaded {name}')
			run_again = input('Download another? y/n: ')
		except Exception as e:
			print(e)
			print(f'There was an error downloading {link}')

	else:
		print('Link not valid!')
		input('Press any key to exit...')
		exit()

	# a loop if the user wants to re-run the program
	while run_again[0].lower() == 'y':
		link = input('Input a YouTube video/playlist link: ')
		input_dest = input('Destination folder (none to keep the same): ')
	
		if input_dest:
			dest = input_dest

			if not os.path.isdir(input_dest):
				try:
					os.mkdir(input_dest)
				except Exception as e:
					print(e)
					print('There was an error creating that destination. Try again.')
					input('Press any key to exit...')
					exit()

		# check if its a video or playlist
		if ('https://' and 'playlist') in link:	
			download_songs_from_playlist(link, dest)
			run_again = input('Download another? y/n: ')
		elif ('https://' and ('watch' or 'https://youtu.be')) in link:
			try:
				name = download_song(link, dest)
				print(f'Downloaded {name}')
				run_again = input('Download another? y/n: ')
			except Exception as e:
				print(e)
				print(f'There was an error downloading {link}')
		else:
			print('Link not valid!')
			input('Press any key to exit...')
			exit()

if __name__ == '__main__':
	main()