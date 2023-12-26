"""
Jhoan Buitrago
01/12/2023 dd/mm/yyyy

https://adventofcode.com/2023/day/2

For each game, check that the amount of cubes doesn't exceed the max amount
for the cubes color.

Sum the game id of all games that do not break this rule.
"""

from sys import stdin


max_value = {"red": 12, "green": 13, "blue": 14}


def main():
    total = 0
    line = stdin.readline()
    game_id = 1
    while line != "":
        _, sets = line.split(":")
        sets = sets.split(";")

        impossible = False 

        for s in sets:
            cubes_data = s.split(",")
            #print(cubes_data)
            for c in cubes_data:
                amount, color = c.strip().split(" ")
                if int(amount) > max_value[color]:
                    impossible = True
                    break
            
            if impossible:
                break
        
        if not impossible:
            total += game_id
            
        line = stdin.readline()
        game_id += 1

    print(total)

        
if __name__ == "__main__":
    main()