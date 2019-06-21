import colors as c
import random
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

Dice_Faces = [dice1 , dice2, dice3, dice4, dice5, dice6]
num_dice = int(input("How many times do you want to roll the dice?"))
for count in range(num_dice):
    random_dice = random.choice(Dice_Faces)   
    print(c.random() + random_dice)

