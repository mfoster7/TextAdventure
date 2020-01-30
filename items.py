import random
class Item:
    #base class for all items
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
#currency items
class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A shiny round coin with {} stamped on the front.",
                         value = 100)
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nAmount: {}\n".format(self.name, self.description, self.value, self.amt)
class Silver(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Silver",
                         description="A slightly tarnished coin with * stamped on the front.",
                         value = 10)
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nAmount: {}\n".format(self.name, self.description, self.value, self.amt)
class Copper(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Copper",
                         description="A dirty cooper coin.",
                         value = 1)
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nAmount: {}\n".format(self.name, self.description, self.value, self.amt)
#piercing melee weapons
class Weapon(Item):
    def __init__(self, name, description, value, min_damage, max_damage):
        self.min_damage = min_damage
        self.max_damage = max_damage
        super().__init__(name, description, value)
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}-{}".format(self.name, self.description, self.value, self.min_damage, self.max_damage)

class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger. At least it has a sharp edge.",
                         value=.5,
                         min_damage=1,
                         max_damage=4)

class shortSword(Weapon):
    def __init__(self):
        super().__init__(name="Shortsword",
                         description="A light finesse weapon. Speed over brawn.",
                         value=5,
                         min_damage=4,
                         max_damage=6)

class handAxe(Weapon):
    def __init__(self):
        super().__init__(name="Hand Axe",
                         description="A small double bladed axe. Can easily be thrown at range.",
                         value=3,
                         min_damage=3,
                         max_damage=5)

class battleAxe(Weapon):
    def __init__(self):
        super().__init__(name="Battle Axe",
                         description="A large two handed axe. Its crushing blows will shatter enemies.",
                         value=12,
                         min_damage=5,
                         max_damage=9)

class longSword(Weapon):
    def __init__(self):
        super().__init__(name="Longsword",
                         description="A heavy two-handed weapon. Crushing blows can shatter bone.",
                         value=15,
                         min_damage=3,
                         max_damage=10)

class Stick(Weapon):
    def __init__(self):
        super().__init__(name="Stick",
                         description="A hefty branch. When all else fails...",
                         value=0,
                         min_damage=1,
                         max_damage=2)
class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A fist sized rock. Slightly more deadly than a stick.",
                         value=0,
                         min_damage=1,
                         max_damage=3)
class Mace(Weapon):
    def __init__(self):
        super().__init__(name="Mace",
                         description="A wooden handle with a large stone head. Powerful bludgeoning tool, but inconsistent.",
                         value=5,
                         min_damage=2,
                         max_damage=7)
