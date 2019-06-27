import colors as c

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
        opponent.hp = opponent.hp - move.damage
        self.hp += move.heal
        self.protection += move.protection

        print(self.Fighter_name + " used " + move.name)
        print("It healed {}hp and gave him {} protection and did {} damage".format(move.heal, move.protection, move.damage))
        print("The opponent now has {} protection and {}hp".format(opponent.protection, opponent.hp))
 
bobs_moves = [Move("Sphere of Protection" , protection=7),
Move("Thorn Strike", damage=10), 
Move("Healing Aura", heal=5)]

bob = Fighter("Bob" , bobs_moves, 25)

peter_moves = [Move("Iron Shield", protection=3),
Move("Earthquake", damage=11),
Move("Healing Aura", heal=6)]

peter = Fighter("Peter" , peter_moves, 30)

selected_move = peter.pick_move()
peter.use_move(selected_move, bob)
