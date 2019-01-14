from random import randint, choice


class Droid:
    body_parts = ["head", "chest", "legs"]

    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def __str__(self):
        return 'Name: {}. Health: {}'.format(self.name, self.health)

    def attack(self, enemy):
        attack_power = randint(1, 15)
        attack_part = choice(self.body_parts)
        defence_power, defence_part = enemy.defence()
        if attack_part == defence_part:
            print('Defence is guessed: {}'.format(defence_part))
            attack_power = attack_power - defence_power
        if attack_power > 0:
            enemy.health -= attack_power

    def defence(self):
        defence_power = randint(5, 10)
        defence_part = choice(self.body_parts)
        return (defence_power, defence_part)


class IronDroid(Droid):
    def strike_with_swort(self):
        print("strike_with_swort")

    def attack(self, enemy):
        self.strike_with_swort()
        return super().attack(enemy)


class SuperDroid(Droid):
    def super_strike(self):
        print("super_strike")

    def attack(self, enemy):
        self.super_strike()
        return super().attack(enemy)


class ElectroDroid(Droid):
    def electro_shock(self):
        print("electro_shock")

    def attack(self, enemy):
        self.electro_shock()
        return super().attack(enemy)


class Arena:
    def __init__(self, droid1, droid2, droid3):
        self.droids = [droid1, droid2, droid3]
        self.round = 0

    def start_battle(self):
        while any(self.droids):
            self.make_round()
        print('Game over')
        print(self.droids[0], self.droids[1], self.droids[2])

    def make_round(self):
        self.round += 1
        print('Round is {}'.format(self.round))
        print(self.droids[0], self.droids[1])
        self.droids[0].attack(self.droids[1])
        self.droids[1].attack(self.droids[2])
        self.droids[2].attack(self.droids[0])


if __name__ == "__main__":
    iro = IronDroid("iron")
    ele = ElectroDroid("electro")
    sup = SuperDroid("super")
    arena = Arena(iro, ele, sup)
    arena.start_battle()
