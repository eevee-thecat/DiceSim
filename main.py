import random
from dataclasses import dataclass


@dataclass
class Die:
    sides: int

    def roll(self):
        return random.randint(1, self.sides)


@dataclass
class DiceSet:
    dice: list[Die]

    def roll(self):
        return [die.roll() for die in self.dice]


def print_set(diceset):
    if not diceset.dice:
        print("\tYour dice set is empty.")
    else:
        for index, die in enumerate(diceset.dice):
            print(f"\t{index + 1}. {die.sides}-sided die")
    print()


def main():
    diceset = DiceSet([])
    bonus = 0

    while True:
        print("Welcome to the dice simulator!")
        print(
            """0. Exit
1. Check the dice in your dice set
2. Add a die to the set
3. Remove a die from the set
4. Change bonus
5. Roll
"""
        )

        entry = int(input("Choose an option: "))
        print()

        if entry == 1:
            print_set(diceset)
        elif entry == 2:
            sides = input(
                "Enter many sides the die has or press Enter to add a 6 sided die: "
            )
            if not sides:
                sides = 6
            else:
                sides = int(sides)
            if sides <= 1:
                print("Please enter a valid number")
                continue
            diceset.dice.append(Die(sides))
        elif entry == 3:
            print_set(diceset)
            remove = int(input("Enter the position of the die you want to remove: "))
            if remove < 1 or remove > len(diceset.dice):
                print("Please enter a valid number")
                continue
            del diceset.dice[remove - 1]
        elif entry == 4:
            print(f"Your current bonus to roll is: {bonus:+}")
            bonus = int(input("Enter the new bonus to roll: "))
        elif entry == 5:
            if not diceset.dice:
                print("No dice to roll, please add some dice first!")
                continue
            rolls = diceset.roll()
            rolls.sort()
            print(f"You rolled {rolls}")
            if bonus != 0:
                print(f"With bonus: {sum(rolls) + bonus}")
            print(f"Before bonus: {sum(rolls)}")
            print(f"Min roll: {min(rolls)}\nMax roll: {max(rolls)}")
            print()
        elif entry == 0:
            print("Goodbye!")
            exit(0)
        else:
            print("Please enter a valid choice")
            print()


if __name__ == "__main__":
    main()
