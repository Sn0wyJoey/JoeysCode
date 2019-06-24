import colors as c
import random
import sys

dice1 ='''|-----------|            
|           |           
|           |
|     .     |
|           |
|___________| 
'''          

dice2 ='''|-----------|            
|           |           
|     .     |
|     .     |
|           |
|___________| 
'''                   
dice3 ='''|-----------|            
|           |           
|     .     |
|     .     |
|     .     |
|___________| 
'''           

dice4 ='''|-----------|            
|           |           
|  .  .     |
|  .  .     |
|           |
|___________| 
'''                   

dice5 ='''|-----------|            
|   .       |           
|  . .      |
|  . .      |
|           |
|___________| 
'''                   

dice6 ='''|-----------|            
|   . .     |           
|   . .     |
|   . .     |
|           |
|___________| 
'''                   
lenth_of_list = len(sys.argv)
num_dice = 0

if lenth_of_list < 2:
    print("you are using one dice")
    num_dice = 1
else: 
    num_dice = int(sys.argv[1])
Dice_Faces = [dice1 , dice2, dice3, dice4, dice5, dice6]
for count in range(num_dice):
    random_dice = random.choice(Dice_Faces)   
    print(c.random() + random_dice)

