import random

class Character:
    def __init__(self):
        self.hull = 100
        self.shields = 100
        self.power_systems = 100
        self.torpedos = 20
        self.speed = 0
        self.evasion = 0
        self.accuracy = random.randrange(0,100)
        self.enemy = "Klingons"
        self.friend = "Enterprise"

    def take_phaserdamage(self):
        damage=random.randrange(0,20)
        if damage < 0:
            print("%s evades attack." % (self.friend))
        elif damage < self.shields:
            self.shields = self.shields - damage
            print('%s receives %s damage to shields' % (self.friend, damage))
        elif damage > self.shields:
            damage = damage - self.shields
            self.shields = 0
            self.hull = self.hull - damage
            print('%s receives %s damage to hull' % (self.friend, damage))

    def take_torpedodamage(self):
        damage = random.randrange(0, 30)
        if damage == 0:
            print("%s evades attack." % (self.friend))
        elif damage < self.shields:
            self.shields = self.shields - damage
            print('%s receives %s damage to shields' % (self.friend, damage))
        elif damage > self.shields:
            damage = damage - self.shields
            self.shields = 0
            self.hull = self.hull - damage
            print('%s receives %s damage to hull' % (self.friend, damage))

    def deal_phaserdamage(self):
        damage = random.randrange(0, 20)
        if my_ship.power_systems < 1:
            print("We're out of Power".format(my_ship.power_systems))
        elif damage == 0:
            print("%s evades attack." % (self.enemy))
        elif damage < self.shields:
            self.shields = self.shields - damage
            print('%s takes %s damage to shields' % (self.enemy, damage))
        elif damage > self.shields:
            damage = damage - self.shields
            self.shields = 0
            self.hull = self.hull - damage
            print('%s takes %s damage to hull' % (self.enemy, damage))

    def deal_torpedodamage(self):
        damage = random.randrange(0, 30)
        if my_ship.torpedos < 1:
            print("We're out of Torpedos!".format(my_ship.torpedos))
        elif damage == 0:
            print("%s evades attack." % (self.enemy))
        elif damage < self.shields:
            self.shields = self.shields - damage
            print('%s takes %s damage to shields' % (self.enemy, damage))
        elif damage > self.shields:
            damage = damage - self.shields
            self.shields = 0
            self.hull = self.hull - damage
            print('%s takes %s damage to hull' % (self.enemy, damage))


    def Phasers(self):
        self.power_systems -= 5

    def Torpedos(self):
        self.torpedos -= 1

    def power_to_shields(self):
        self.shields += 15
        self.power_systems -= 10

    def increase_speed(self):
        self.speed += 1
        #proc = subprocess.Popen(['animate', 'C:\Test\increase_speed.gif'])
        #proc.communicate()

    def evasion(self):
        self.evasion = self.speed * 10

    def accuracy(self):
        self.accuracy = self.accuracy - self.evasion

class Enterprise(Character):
    def __init__(self):
        Character.__init__(self)

    def say_state(self):
        print("Hull at {}%".format(self.hull))
        print("Shields at {}%".format(self.shields))
        print("Remaining Power at {}%".format(self.power_systems))
        print("We are at Warp {}".format(self.speed))


class Klingons(Character):
    def __init__(self):
        Character.__init__(self)


    def say_state(self):
        print("Klingon Hull at {}%".format(self.hull))
        print("Klingon Shields at {}%".format(self.shields))


if __name__ == '__main__':
    my_ship = Enterprise()
    enemy_ship = Klingons()
    Enterprise = True
    Klingon = True
    run_game = True
    print("The Enterprise is under attack!")
    while run_game:
        action = input\
            ("What should we do Captain? Fire [P]hasers, Fire [T]orpedoes, "
             "[D]amage Report, [E]nemy Ship Status, Power to [S]heilds, [I]ncrease Speed?").upper()
        if action not in "PTDESI" or len(action) != 1:
            print("Say again Captain?")
        if action == 'P':
            my_ship.Phasers()
            enemy_ship.deal_phaserdamage()
            my_ship.take_phaserdamage()
            if my_ship.power_systems > 0:
                print("Power Systems down to {}".format(my_ship.power_systems))
        elif action == 'T':
            my_ship.Torpedos()
            enemy_ship.deal_torpedodamage()
            my_ship.take_torpedodamage()
            if my_ship.torpedos > 0:
                print("We have {} Torpedos left".format(my_ship.torpedos))
        elif action == 'D':
            my_ship.say_state()
        elif action == 'E':
            enemy_ship.say_state()
        elif action == 'S':
            my_ship.power_to_shields()
            print('Shields increased to {}'.format(my_ship.shields))
            print('Remaining Power Systems at {}'.format(my_ship.power_systems))
        elif action == 'I':
            my_ship.increase_speed()
            if my_ship.speed < 9:
                print('Speed increased to Warp {}'.format(my_ship.speed))
            if my_ship.speed > 8:
                print('We''re at maximum Warp Captain!'.format(my_ship.speed))
        if my_ship.hull <= 0:
            my_ship = False
            print("Enterprise Destroyed!")
            run_game = False
            break
        if enemy_ship.hull <= 0:
            enemy_ship = False
            print("Klingons Destroyed!")
            run_game = False
            break