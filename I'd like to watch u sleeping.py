import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("Aku banyak takutnya", 0.1),
        ("Misalnya", 0.1),
        ("Kehilangan dirimu sekali lagi dan patah hati", 0.1),
        ("Perasaan sendiri bukan hal yang aku suka", 0.1),
        ("Hal yang paling kusuka, di dekatmu", 0.1),
        ("Kau adalah orang favoritku nomor satu", 0.1),
        ("Nomor 2, 3, 4 5, 6 isinya namamu", 0.2),
        ("Huruf besar semuaaaaaaaaaaaaaa", 0.1)
    ]
    delays = [0.5, 5.0, 6.0, 13.0, 21.0 , 26.0, 31.0, 40.0]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()