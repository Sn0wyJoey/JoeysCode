import time
import colors
timer = 0
try:
    while True:
        timer += 1
        time.sleep(1)
except KeyboardInterrupt:
    print("The timer ended at", timer,"seconds")