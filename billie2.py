from playsound import playsound
from threading import Thread

#playsound('copycat.mp3')

def play_music():
    playsound('copycat.mp3')

# play music in background with separate Thread
music_thread = Thread(target=play_music)
music_thread.start()

print('What is Taylor Swift album "Reputation" about?')
user_input = input('What is your guess?')
print('You guessed:' + user_input)
