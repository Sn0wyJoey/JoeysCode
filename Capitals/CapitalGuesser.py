from tkinter import Tk, simpledialog, messagebox

def getInfo():
    data = {}
    with open('capitals.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, capital = line.split('/')
            country = country.lower()
            # Store the country name as the key and the country capital as the value in the data dictionary 
            data[country] = capital
    return data

def addInfo(country, capital):
    with open('capitals.txt', 'a') as file: # a for append
        file.write(f'\n{country}/{capital}') # Add a country and capital on a new line
    
# Hide the window that Tkinter automatically creates
root = Tk()
root.withdraw()

# Get info about capitals
World = getInfo()

# Start infinite loop
while True: 
    try:  
        getCountry = simpledialog.askstring('Country', 'Type any country here:').lower()
        if getCountry in World:
            result = World[getCountry]
            messagebox.showinfo('Capital', 'The capital city of ' + getCountry + ' is ' + result)
        else:
            newCapital = simpledialog.askstring('Tell me...', 'I don\'t know that! What is the capital city of ' + getCountry + '?').lower().capitalize()
            addInfo(getCountry, newCapital)
            World[getCountry] = newCapital
    except AttributeError:
            print('Exited program')
            exit()
