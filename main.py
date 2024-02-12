from Scripts.Characters import Character, characters
from Scripts.Items import Item
from Scripts.Actions import Action
from Scripts.CombatWindow import CombatWindow


class GameManager:  # handle the game loop and other managers
    def __init__(self):
        self.windows = []

        self.itemmanager = ItemsManager(self)
        self.charactermanager = CharacterManager(self)
        self.mapmanager = None
        self.combatmanager = None

        self.init_battle()
        self.update_all()
        self.run_all()

    def run_all(self):
        for w in self.windows:
            w.run()

    def close_all(self):
        for w in self.windows:
            w.end()

    def update_all(self):
        for w in self.windows:
            try:
                w.update()
            except:
                pass

    def init_battle(self):
        self.charactermanager.spawn(self.charactermanager.data["Barrel"])
        self.charactermanager.spawn(self.charactermanager.data["Barrel"])
        self.combatmanager = CombatManager(self, [self.charactermanager.characters["Barrel"]],
                                           [self.charactermanager.characters["Barrel 2"]])


class MapManager:  # handle map (movement and position)
    def __init__(self, manager):
        self.map = []
        for y in range(10):
            self.map.append([])
            for x in range(10):
                self.map[-1].append([])

        self.mapwindow = CombatWindow(manager, self)
        manager.windows.append(self.mapwindow)

    def get_tile(self, coord):
        return self.map[coord[1]][coord[0]]

    def remove(self, character):
        test = self.get_character_coord(character)
        if test:
            self.get_tile(test).remove(character)
            return character
        return False

    def insert(self, character, coord):
        if not self.check_occupy(coord):
            self.remove(character)
            self.get_tile(coord).append(character)

    def get_character_coord(self, character):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if character in self.get_tile((x, y)):
                    return x, y
        return False

    def check_occupy(self, coord):
        for c in self.get_tile(coord):
            if "large" in c.trait:
                return c
        return False


class CharacterManager:  # handle characters (spawning and referencing)
    def __init__(self, manager):
        self.characters = {}
        self.data = {c.__name__: c for c in characters}

    def append(self, character: Character):
        if character.name in self.characters:
            character.name += " 2"
        while character.name in self.characters:
            character.name = character.name[:-1] + str(int(character.name[-1]) + 1)
        self.characters[character.name] = character

    def spawn(self, characterclass: type):
        if issubclass(characterclass, Character):
            self.append(characterclass())


class ItemsManager:  # handle items (referencing and equipping)
    def __init__(self, manager):
        pass


class CombatManager:  # handle combat (loop and interactions)
    def __init__(self, manager: GameManager, ally: list, enemy: list):
        self.mapmanager = MapManager(manager)
        if len(ally) > 5:
            ally = ally[:4]
        if len(enemy) > 5:
            enemy = enemy[:4]
        for i in range(len(ally)):
            self.mapmanager.insert(ally[i], (0, i))
        for i in range(len(enemy)):
            self.mapmanager.insert(enemy[i], (9, i))


if __name__ == '__main__':
    manager = GameManager()
