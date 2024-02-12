import inspect
import sys


stats = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]


class Character:
    def __init__(self, name, hp, traits, **stat):
        self.name = name
        self.maxhp = hp
        self.hurt = 0

        self.stat = stat
        for s in stats:
            if s not in self.stat:
                self.stat[s] = 0

        self.trait = traits

    def __repr__(self):
        return self.name


class Barrel(Character):
    def __init__(self):
        super().__init__("Barrel", 1, ["large", "pickup", "environment"])


def init_characters():
    char = inspect.getmembers(sys.modules[__name__],
                              lambda member: inspect.isclass(member) and member.__module__ == __name__)
    return [c[1] for c in char if c[1].__name__ != Character.__name__]

characters = init_characters()
print(characters)
for i in characters:
    print(type(i))
