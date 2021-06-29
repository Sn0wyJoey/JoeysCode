#lets create a countdown to zero. Once we reach zero, we print something.
#lets import time so that we can wait a second after each countdown
import time

for n in range(10, 0, -1): #starting point is 10, ending point is 0, step is -1 (it is -1 because we are counting down)
    print(n)
    time.sleep(1) #pauses for 1 second using the sleep function

print("Happy New Year!")