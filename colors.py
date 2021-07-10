import random as r

reset = '\u001b[0m'
black = '\u001b[30m'
red = '\u001b[31m'
green = '\u001b[32m'
yellow = '\u001b[33m'
blue = '\u001b[34m'
magenta = '\u001b[35m'
cyan = '\u001b[36m'
white = '\u001b[37m'

bright_black = '\u001b[30;1m'
bright_red = '\u001b[31;1m'
bright_green = '\u001b[32;1m'
bright_yellow = '\u001b[33;1m'
bright_blue = '\u001b[34;1m'
bright_magenta = '\u001b[35;1m'
bright_cyan = '\u001b[36;1m'
bright_white = '\u001b[37;1m'

background_black = '\u001b[40m'
background_red = '\u001b[41m'
background_green = '\u001b[42m'
background_yellow = '\u001b[43m'
background_blue = '\u001b[44m'
background_magenta = '\u001b[45m'
background_cyan = '\u001b[46m'
background_white = '\u001b[47m'

background_bright_black = '\u001b[40;1m'
background_bright_red = '\u001b[41;1m'
background_bright_green = '\u001b[42;1m'
background_bright_yellow = '\u001b[43;1m'
background_bright_blue = '\u001b[44;1m'
background_bright_magenta = '\u001b[45;1m'
background_bright_cyan = '\u001b[46;1m'
background_bright_white = '\u001b[47;1m'

bold = '\u001b[1m'
underline = '\u001b[4m'
reversedcolor = '\u001b[7m'

b_black = background_black
b_red = background_red
b_green = background_green
b_yellow = background_yellow 
b_blue = background_blue
b_magenta = background_magenta
b_cyan = background_cyan
b_white = background_white

br_black = bright_black
br_red = bright_red
br_green = bright_green
br_yellow = bright_yellow
br_blue = bright_blue
br_magenta = bright_magenta
br_cyan = bright_cyan
br_white = bright_white

re = reset
clear = reset

def random_color():
    randomColor = r.choice([red, green, yellow, blue, magenta, cyan, white])
    return randomColor

rc = random_color

def random_background():
    randomBackround = r.choice([background_red, background_green, background_yellow, background_blue, background_magenta, background_cyan, background_white])
    return randomBackround
rb = random_background

def random_all():
    randomAll = r.choice([reset, red, green, yellow, blue, magenta, cyan, white, bright_red, bright_green, bright_yellow, bright_blue, bright_magenta, bright_cyan, bright_white, background_red, background_green, background_yellow, background_blue, background_magenta, background_cyan, background_white, background_bright_red, background_bright_green, background_bright_yellow, background_bright_blue, background_bright_magenta, background_bright_cyan, background_bright_white])
    return randomAll

random = random_all
ra = random_all

def multi_color(text):
    z = ''
    for count in range(len(text)):
        z += rc() + text[count] + re
    return z

mc = multi_color

def multi_backround(text):
    z = ''
    for count in range(len(text)):
        z += rb() + text[count] + re
    return z

mb = multi_backround

def multi_all(text):
    z = ''
    for count in range(len(text)):
        z += ra() + text[count] + re
    return z

ma = multi_all