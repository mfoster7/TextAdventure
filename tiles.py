import random, enemies, items, world, actions
random_amt = random.randint(10,30)
class MapTile:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplimentedError()

    def modify_player(self, player):
        raise NotImplimentedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.ViewWeaponInventory())
        return moves

class StartingRoom(MapTile):
    def intro_text(self):
        return"""
        You find yourself in a cave with nothing but torch light flickering
        off the walls. Four paths await you, each as dark and foreboding as the next.\n """
    def modify_player(self, player):
        #Room has no action on player
        pass

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
    def add_loot(self, player):
        for i in player.inventory:
            print(i)
            if self.item == i:
                i.amt + self.item.amt
    def modify_player(self, player):
        self.add_loot(player)

class WeaponRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
    def add_weapon(self, player):
        player.weapon_inventory.append(self.item)
    def modify_player(self, player):
        self.add_weapon(player)

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
    def modify_player(self, player):
        if self.enemy.is_alive():
            random_dam = (random.randint(self.enemy.damage1,self.enemy.damage2))
            player.hp = player.hp - random_dam
            print("\tThe {} does {} damage. You have {} HP remaining.\n".format(self.enemy.name, random_dam, player.hp))
    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You forge onward."""

    def modify_player(self, player):
        #Room has no action
        pass

class FindGoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(random_amt))
    def intro_text(self):
        return """
        You find a pouch filled with {} shiny gold coins!""".format(random_amt)

class BanditRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Bandit())
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A masked Bandit stands in your path."""
        else:
            return """
            The body of the Bandit lies on the cave floor."""

class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A Giant Spider bursts forth! It's ensnaring webs coat the cave walls."""
        else:
            return """
            The husk of the Spider is crumpled on the cave floor."""

class BeholderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Orc())
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A large floating orb stares into your soul. Its long tenticles look towards you."""
        else:
            return """
            The Beholder lets out a terrible screech and comes crashing to the floor, rolling towards you."""

class OrcRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Orc())
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A grotesque looking creature charges at you."""
        else:
            return """
            The Orcs black blood covers the cave floor."""

class ZombieRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Zombie())
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A rotting corpse turns it head to look towards you, it draws a mangled steel blade."""
        else:
            return """
            The Zombies rotting flesh falls to cave floor, more lifeless than before."""

class FindDaggerRoom(WeaponRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())
    def intro_text(self):
        return """
        Something shines against the dark floor. A small blade!

                    ===)-------

        More suitable than a stick or rock. """

class FindShortSwordRoom(WeaponRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.shortSword())
    def intro_text(self):
        return """
        A shiny blade lays on the cave floor. It's a short sword!

                                  ./~
                        (=#######=[}===============>
                                  `\_

        Reliable and quick, this weapon may be the difference between life and death. """

class FindLongSwordRoom(WeaponRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.longSword())
    def intro_text(self):
        return """
        A large blade is stuck in a rotting corpse.
        Grabbing the hilt with both hands, you pull the longsword out.

                              |
                    O=========|>>>>>>>>>>>>>>>>>>>>>>>>>>
                              |

        This heavy two handed beast will frighten anything it meets. """

class FindHandAxeRoom(WeaponRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.handAxe())
    def intro_text(self):
        return """
        A small double bladed axe sticks out of a chunk of rotting wood.

                                  /`-||-'\
                                 | -=||=- |
                                  \,-||-./
                                     ||
                                     ||
                                     ||

        Small but sharp, this quick weapon is versitile and can be thrown at range. """

class FindBattleAxeRoom(WeaponRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.battleAxe())
    def intro_text(self):
        return """
        A heavy two handed axe rests again the bones of a once deadly warrior.

                                 //`-||-'\\
                                (| -=||=- |)
                                 \\,-||-.//
                                     ||
                                     ||
                                     ||
                                     ||
                                     ||
                                     ||
                                     ()

        A mix of bludgeoning and slicing, this weapon brings pain when swung by the proper weilder. """

class FindRockRoom(WeaponRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Rock())
    def intro_text(self):
        return """
        A large rock on the floor catches your eye. It seems suitable for bludgeoning.
        A barbaric bludgeoning tool but deadly none the less."""

class FindMaceRoom(WeaponRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Mace())
    def intro_text(self):
        return """
        A pile of bones in the corner is holding some type of weapon.
                                         ____
                                       </   ^\
                        (@@@@@@@@@@@@@@| ^    |>
                                       <\____/>

        You pick up the heafty mace. This weapon will easily smash apart bone."""

class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!

        Victory is yours!"""

    def modify_player(self, player):
        player.victory = True
