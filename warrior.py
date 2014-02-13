
def add_weapon(func):
    def inner(warrior):
        damage = warrior.damage
        for w in warrior.weapon:
            warrior.damage += w.attack
        func(warrior)
        warrior.damage = damage
    return inner


class Warrior(object):

    def __init__(self, damage):
        self.damage = damage
        self.sword = None
        self.bow = None
        self.mace = None
        self.spear = None
        self.weapon = []

    def get_sword(self):
        if not self.sword:
            self.sword = Sword()
            self.weapon.append(self.sword)

    def get_bow(self):
        if not self.bow:
            self.bow = Bow()
            self.weapon.append(self.bow)

    def get_spear(self):
        if not self.spear:
            self.spear = Spear()
            self.weapon.append(self.spear)

    def get_mace(self):
        if not self.mace:
            self.mace = Mace()
            self.weapon.append(self.mace)

    @add_weapon
    def attack(self):
        print 'Damage: %d ' % self.damage


class Sword(object):
    attack = 10


class Bow(object):
    attack = 15


class Spear(object):
    attack = 20


class Mace(object):
    attack = 25
