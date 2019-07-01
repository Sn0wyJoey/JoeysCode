import colors as c
import time as t
def play_game(p1, p2):
    while True:
        #p1 turn
        print("It is your turn, " + p1.Fighter_name)
        selected_move = p1.pick_move()
        p1.use_move(selected_move, p2)
        if p2.hp <= 0:
            winner = p1.Fighter_name
            return winner

        #p2 turn
        print("It is your turn, " + p2.Fighter_name)
        selected_move = p2.pick_move()
        p2.use_move(selected_move, p1)
        if p1.hp <= 0:
            winner = p2.Fighter_name
            return winner
class Move:
    def __init__(self, name, protection=0, damage=0, heal=0):
        self.name = name
        self.protection = protection
        self.damage = damage
        self.heal = heal

class Fighter:
    def __init__(self, name, moves, hp):
        self.possible_moves = moves
        self.Fighter_name = name
        self.hp = hp
        self.protection = 0
        self.say_name()
    def pick_move(self):
        counter = 0
        print("Pick the number of the move you want")
        for move_choice in self.possible_moves:
            print(counter, move_choice.name)
            counter += 1

        move_num = int(input("What move do you want to use? "))
        return move_num

    def say_name(self):
        print("Hello my name is " + self.Fighter_name)

    def use_move(self, index, opponent):
        move = self.possible_moves[index]
        reduced_damage = 0
        if move.damage > opponent.protection:
            opponent.protection = 0
            reduced_damage = move.damage - opponent.protection
        else:
            self.protection -= move.damage
        opponent.hp -= reduced_damage
        self.hp += move.heal
        self.protection += move.protection
        t.sleep(0.5)
        print(c.clear)
        print(self.Fighter_name + " used " + move.name)
        print(self.Fighter_name + ":" + c.green + str(self.hp) + " Hit points\t" + c.blue + str(self.protection) + " Protection" + c.reset)
        print(opponent.Fighter_name + ":" + c.green + str(opponent.hp) + " Hit points\t" + c.blue + str(opponent.protection) + " Protection" + c.reset)
        print("\n")

bobs_moves = [Move("Sphere of Protection" , protection=7),
Move("Thorn Strike", damage=10), 
Move("Healing Aura", heal=5)]


peter_moves = [Move("Iron Shield", protection=3),
Move("Earthquake", damage=999),
Move("Healing Aura", heal=6)]

winner = "Nobody"

go_again = "yes"
while go_again in ["yes", "yea", "sure" , "ok"]:
    bob = Fighter("Bob" , bobs_moves, 25)
    peter = Fighter("Peter" , peter_moves, 30)
    winner = play_game(bob, peter)
    print("The winner is " + winner)
    go_again = input("Do you want to go again? ")
    print(c.clear)

print("Thank you for playing!")