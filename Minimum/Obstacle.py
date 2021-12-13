from rich import print as rprint
from math import floor, pi, e
from typing import List

# Known:
# Triangular prism, 3 faces
# Colors are assigned counter-clockwise: f1 > f2 > f3
# Six puzzles with predefined formulas

# FACES
f1: List[int] = []  # front
f2: List[int] = []  # back on the right
f3: List[int] = []  # back on the left

# PUZZLES
puzzleOne: List[List[int]] = []
puzzleTwo: List[List[int]] = []
puzzleThree: List[List[int]] = []
puzzleFour: List[List[int]] = []
puzzleFive: List[List[int]] = []
puzzleSix: List[List[int]] = []

########################   INTRO   ########################


def intro():
    rprint("[bold blue]Instant Insanity Puzzle[/bold blue]\n")
    rprint("[blue]Generating colors with the given contraints ...[/blue]")

    slices = len(puzzleOne)
    rprint("[blue]Assigning counterclockwise to " + str(slices) +
           " slices ...[/blue]\n")  # should be 31 slices
    p = [puzzleOne, puzzleTwo, puzzleThree, puzzleFour, puzzleFive, puzzleSix]
    f = [
        "1 + ((floor n * 17 pi^6)mod 31)", "1 + ((floor n * 17 e^6)mod 31)", " 1 + ((floor n * 17 e^8)mod 31)",
        "1 + ((floor n * 11 e^8)mod 31)", "1 + ((floor n * 101 e^2)mod 31)", "1 + ((floor n * 101 e^8)mod 31)"
    ]
    p_number = 0
    for i in p:
        p_number = p_number+1
        rprint("\n[bold green]Puzzle " + str(p_number) +
               ": " + f[p_number-1] + "[/bold green]")

        # prints colors [ color of face 1, color of face 2, color of face 3]
        print(p[p_number-1])


# Colors
# Puzzle 1: 1 + ((floor n * 17 pi^6)mod 31) ~ 1 + ((floor(n * (17 * pow(pi, 6)))) % 31)
# Puzzle 2: 1 + ((floor n * 17 e^6)mod 31) ~ 1 + ((floor(n * (17 * pow(e, 6)))) % 31)
# Puzzle 3: 1 + ((floor n * 17 e^8)mod 31) ~ 1 + ((floor(n * (17 * pow(e, 8)))) % 31)
# Puzzle 4: 1 + ((floor n * 11 e^8)mod 31) ~ 1 + ((floor(n * (11 * pow(e, 8)))) % 31)
# Puzzle 5: 1 + ((floor n * 101 e^2)mod 31) ~ 1 + ((floor(n * (101 * pow(e, 2)))) % 31)
# Puzzle 6: 1 + ((floor n * 101 e^8)mod 31) ~ 1 + ((floor(n * (101 * pow(e, 8)))) % 31)

# Start: 1
# End: 32 (essentially 31 iterations since we end at 1)
# Step: 1 (default)
for n in range(1, 32):
    puzzleOne.append([1 + ((floor(n * (17 * pow(pi, 6)))) % 31), 1 + ((floor((n+1)
                     * (17 * pow(pi, 6)))) % 31), 1 + ((floor((n+2) * (17 * pow(pi, 6)))) % 31)])
    puzzleTwo.append([1 + ((floor(n * (17 * pow(e, 6)))) % 31), 1 + ((floor((n+1)
                     * (17 * pow(e, 6)))) % 31), 1 + ((floor((n+2) * (17 * pow(e, 6)))) % 31)])
    puzzleThree.append([1 + ((floor(n * (17 * pow(e, 8)))) % 31), 1 + ((floor(
        (n+1) * (17 * pow(e, 8)))) % 31), 1 + ((floor((n+2) * (17 * pow(e, 8)))) % 31)])
    puzzleFour.append([1 + ((floor(n * (11 * pow(e, 8)))) % 31), 1 + ((floor(
        (n+1) * (11 * pow(e, 8)))) % 31), 1 + ((floor((n+2) * (11 * pow(e, 8)))) % 31)])
    puzzleFive.append([1 + ((floor(n * (101 * pow(e, 2)))) % 31), 1 + ((floor(
        (n+1) * (101 * pow(e, 2)))) % 31), 1 + ((floor((n+2) * (101 * pow(e, 2)))) % 31)])
    puzzleSix.append([1 + ((floor(n * (101 * pow(e, 8)))) % 31), 1 + ((floor((n+1)
                     * (101 * pow(e, 8)))) % 31), 1 + ((floor((n+2) * (101 * pow(e, 8)))) % 31)])


if __name__ == '__main__':
    intro()
