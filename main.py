from pyfiglet import Figlet
import config

dndconf = config.Config.MENU_OPTIONS

import diceroll.dice as dice
dndconf["dice"] = {
    "name": "Dice Roller",
    "app": dice
}


f = Figlet(font="big")
print(f.renderText('DND-Tools'))


def main():
    print(dice.rolldice("2d10k10"))
    print("-------")
    # print(dice.rolldice("4d6d2"))
    # print("-------")
    # print(dice.rolldice("5d5k"))
    # print("-------")
    # print(dice.rolldice("5d8+2-1d6"))
    # print("-------")
    # print(dice.rolldice("Hello"))
    print(dice.rolldice("10d1"))



if __name__ == "__main__":
    main()