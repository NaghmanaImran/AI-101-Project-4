import time

def countdown_timer(seconds):
    if seconds >= 0:
        mins, secs = divmod(seconds, 60)
        print(f'{mins:02d}:{secs:02d}', end='\r')
        time.sleep(1)
        countdown_timer(seconds - 1)
    else:
        print("Time's up!")

if __name__ == '__main__':
    countdown_timer(10)