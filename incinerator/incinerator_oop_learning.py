class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.max_health = self.health

    @property
    def is_alive(self) -> bool:
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 3
        self.health = 60
        self.defense = 2
        self.max_health = self.health


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 4
        self.health = 40
        self.vampirism = 50
        self.max_health = self.health


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6


class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 0
        self.health = 60
        self.max_health = self.health

    def heal(self, unit):
        unit.health += 2
        if unit.health > unit.max_health:
            unit.health = unit.max_health


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        true_attack = unit_1.attack
        if type(unit_2) is Defender:
            if unit_2.defense < unit_1.attack:
                true_attack -= unit_2.defense
            else:
                true_attack = 0
        if type(unit_1) is Vampire:
            unit_1.health += true_attack * (unit_1.vampirism / 100)
        unit_2.health -= true_attack
        if unit_2.is_alive:
            true_attack = unit_2.attack
            if type(unit_1) is Defender:
                if unit_1.defense < unit_2.attack:
                    true_attack -= unit_1.defense
                else:
                    true_attack = 0
            if type(unit_2) is Vampire:
                unit_2.health += true_attack * (unit_2.vampirism / 100)
            unit_1.health -= true_attack
    return unit_1.is_alive


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_type: Warrior or Knight, amount: int):
        for _ in range(amount):
            self.units.append(unit_type())


class Battle:
    def fight(self, army_1: Army, army_2: Army) -> bool:
        while True:
            index_army_1 = None
            index_army_2 = None
            for index, unit in enumerate(army_1.units):
                if unit.is_alive:
                    index_army_1 = index
                    break
            for index, unit in enumerate(army_2.units):
                if unit.is_alive:
                    index_army_2 = index
                    break
            if index_army_1 is None:
                return False
            elif index_army_2 is None:
                return True
            else:
                unit_1, unit_2 = army_1.units[index_army_1], army_2.units[index_army_2]
                while unit_1.is_alive and unit_2.is_alive:
                    true_attack = unit_1.attack
                    if type(unit_2) is Defender:
                        if unit_2.defense < unit_1.attack:
                            true_attack -= unit_2.defense
                        else:
                            true_attack = 0
                    if type(unit_1) is Vampire:
                        unit_1.health += true_attack * (unit_1.vampirism / 100)
                    if (type(unit_1) is Lancer) and ((index_army_2 + 1) < len(army_2.units)):
                        army_2.units[index_army_2 + 1].health -= true_attack * 0.5
                    if (index_army_1 + 1) < len(army_1.units):
                        if type(army_1.units[index_army_1 + 1]) is Healer:
                            army_1.units[index_army_1 + 1].heal(unit_1)
                    unit_2.health -= true_attack
                    if unit_2.is_alive:
                        true_attack = unit_2.attack
                        if type(unit_1) is Defender:
                            if unit_1.defense < unit_2.attack:
                                true_attack -= unit_1.defense
                            else:
                                true_attack = 0
                        if type(unit_2) is Vampire:
                            unit_2.health += true_attack * (unit_2.vampirism / 100)
                        if (type(unit_2) is Lancer) and ((index_army_1 + 1) < len(army_1.units)):
                            army_1.units[index_army_1 + 1].health -= true_attack * 0.5
                        if (index_army_2 + 1) < len(army_2.units):
                            if type(army_2.units[index_army_2 + 1]) is Healer:
                                army_2.units[index_army_2 + 1].heal(unit_2)
                        unit_1.health -= true_attack


if __name__ == "__main__":
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()
    priest = Healer()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True
    assert freelancer.health == 14
    priest.heal(freelancer)
    assert freelancer.health == 16

    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
