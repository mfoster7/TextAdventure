import random
class Enemy:
    def __init__(self, name, hp, damage1, damage2):
        self.name = name
        self.hp = hp
        self.damage1 = damage1
        self.damage2 = damage2
    def is_alive(self):
        return self.hp > 0

class Bandit(Enemy):
    def __init__(self):
        super().__init__(name="Bandit", hp=10, damage1=0, damage2=3)

class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=20, damage1=2, damage2=10)

class Orc(Enemy):
    def __init__(self):
        super().__init__(name="Orc", hp=20, damage1=2, damage2=5)

class Beholder(Enemy):
    def __init__(self):
        super().__init__(name="Beholder", hp=50, damage1=9, damage2=30)

class GelatinousCube(Enemy):
    def __init__(self):
        super().__init__(name="Gelatinous Cube", hp=30, damage1=15, damage2=15)

class Zombie(Enemy):
    def __init__(self):
        super().__init__(name="Zombie", hp=15, damage1=3, damage2=6)

class Orc(Enemy):
    def __init__(self):
        super().__init__(name="Orc", hp=15, damage1=3, damage2=6)
