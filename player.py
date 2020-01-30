import items, world, enemies, game, actions
import random

class Player:
    def __init__(self):
        self.inventory = [items.Gold(15), items.Silver(50), items.Copper(100)]
        self.weapon_inventory = [items.Stick()]
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def print_weapon_inventory(self):
        for item in self.weapon_inventory:
            print(item, '\n')

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        max_dmg = 0
        for i in self.weapon_inventory:
            if(i.max_damage > max_dmg):
                max_dmg = i.max_damage
                best_weapon = i
        attack_dmg = random.randint(best_weapon.min_damage, best_weapon.max_damage)
        print("\tYou use {} against {}! It did {} damage!".format(best_weapon.name, enemy.name, attack_dmg))
        enemy.hp -= attack_dmg
        if not enemy.is_alive():
            print("\tYou killed {}!\n".format(enemy.name))
        else:
            print("\t{} HP is {}.".format(enemy.name, enemy.hp))

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        #if(game.getLastAction() == "w"):
        #    self.move_south()
        #if(game.getLastAction() == "f"):
        #    self.move_north()
        #if(game.getLastAction() == "a"):
        #    self.move_east()
        #if(game.getLastAction() == "d"):
        #    self.move_west()
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)
