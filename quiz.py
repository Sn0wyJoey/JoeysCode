import colors as c
import random as r
import time as t

def ask(text):
    answer = input(text + " >> ").lower()
    return answer

q1 = None
q2 = None
q3 = None
score = 0

a1 = ['a', 'b', 'c', 'd', 'e']
a2 = ['a', 'b', 'c', 'd', 'e']
a3 = ['a', 'b', 'c', 'd', 'e']

print(c.bold + c.rc() + 'Welcome ' + c.rc() + 'to ' + c.rc() + 'this ' + c.rc() + 'quiz!' + c.bright_red + ' To start, answer the questions:\n' )
t.sleep(0.7)

while q1 not in a1:
    q1 = ask(c.bold + c.rc() + 'Which of these countries were neutral in both world wars?' + c.yellow + """

A)""" + c.red + '                          Switzer' + c.white + 'land' + c.yellow + """
B)""" + c.red + '                          I' + c.white + 'ra' + c.green + 'n' + c.yellow + """
C)""" + c.blue + '                          Swed' + c.yellow + 'en' + c.yellow + """
D)""" + c.red + '                          Au' + c.white + 'str' + c.red + 'ia' + c.yellow + """
E)""" + c.red + '                          A,' + c.green + ' B' + c.white + ' and' + c.cyan + ' C' + c.yellow + """

---------------------------[1/3]----------------------""")
t.sleep(0.7)

while q2 not in a2:
    q2 = ask('\n' + c.bold + c.rc() + 'What is 50 * 50 (50 times 50)?' + c.yellow + """

A)""" + c.blue + '                          25' + c.yellow + """
B)""" + c.blue + '                          2500' + c.yellow + """
C)""" + c.blue + '                          250' + c.yellow + """
D)""" + c.blue + '                          350' + c.yellow + """
E)""" + c.blue + '                          35' + c.yellow + """

---------------------------[2/3]----------------------""")
t.sleep(0.7)

while q3 not in a3:
    q3 = ask('\n' + c.bold + c.rc() + 'When did the USA gain their independance? (Answer in A, B, C, D or E)' + c.yellow + """

A)""" + c.blue + '                          July' + c.red + ' 4th, ' + c.white + '1776' + c.yellow + """
B)""" + c.blue + '                          July' + c.red + ' 4th, ' + c.white + '1775' + c.yellow + """
C)""" + c.blue + '                          July' + c.red + ' 4th, ' + c.white + '1778' + c.yellow + """
D)""" + c.blue + '                          July' + c.red + ' 4th, ' + c.white + '1779' + c.yellow + """
E)""" + c.blue + '                          July' + c.red + ' 4th, ' + c.white + '1773' + c.yellow + """

---------------------------[3/3]----------------------""")
t.sleep(0.5)

if q1 in 'e':
    score += 1
if q2 in 'c':
    score += 1
if q3 in 'a':
    score += 1



print(c.clear + c.magenta + '\nCongradulations! You finished the quiz! Here are your results:'
 + c.mc('\nYou got ' + str(score) + '/3 correct!')
 + '\nAnswers: ' + c.clear + c.bold + c.black + c.background_white + 'ECA' + c.clear)
print(c.magenta + 'Your answers: ' + c.clear + c.bold + c.black + c.background_white, end = '')
print(str(q1.upper() + q2.upper() + q3.upper()))





