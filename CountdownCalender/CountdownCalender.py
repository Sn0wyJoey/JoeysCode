from tkinter import Tk, Canvas
from datetime import date, datetime

def get_events():
    events = []
    with open('events.txt') as file:
        for line in file: # for every line in the file
            line = line.rstrip('\n') # Remove the '\n' character from the end of each line in the file
            currentEvent = line.split(',') # Split the strings into two at the comma and adds them to a list
            currentEvent[1] = datetime.strptime(currentEvent[1], '%d/%m/%y').date() # Turns the date in currentEvents from a string to a date
            events.append(currentEvent)
    return events

def days_left(date1, date2):
    daysLeft = str(date1 - date2)
    numDays = daysLeft.split(' ')
    return numDays[0]

# Start Canvas:
root = Tk()
c = Canvas(root, width = 1000, height = 800, bg = 'black') # Creates a canvas called c
c.pack() # Packs the canvas into the tkinter window
c.create_text(500, 50, anchor = 'n', fill = 'orange', font = 'Arial 40 bold underline', text = 'Countdown Calander') # Creates some text

# Calculate the number of days left from each event and add them into a list of lists
events = get_events()
daysLeft = []
for count in range(len(events)):
    daysLeft.append([events[count][0], days_left(events[count][1], date.today())])

# Display the amount of days left
colors = ['lightblue', 'cyan', 'dodger blue', 'blue'] 
y = 130
for count in range(len(daysLeft)):
    displayText = f'It is {daysLeft[count][1]} days until your {daysLeft[count][0]}'
    c.create_text(30, y, anchor = 'w', fill = colors[count%len(colors)], font = 'Arial 32 bold', text = displayText)
    y += 50

# End:
root.mainloop()