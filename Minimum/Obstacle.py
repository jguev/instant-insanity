from rich import print as rprint
from math import floor, pi, e
from typing import List, Dict

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

# Counting unique occurrences
checked: Dict[int, List[List[int]]]


def rules(puzzle: List[List[int]]) -> bool:
    #global checked
    checked = {}
    counter = 0
    abides: bool = True
    for value in puzzle:
        counter = counter+1
        rprint("[bold blue]\n\nChecking slice " +
               str(counter) + "... [/bold blue]\n")
        # if (face 1) is a unique color place in checked
        if value[0] not in checked:
            checked[value[0]] = []
            rprint("[bold blue]> " + str([value[0]]) +
                   " Passed! [/bold blue]\n")
        else:
            rprint("[red]> Duplicate found: " + str(value[0]) + "[/red]\n")
        # face 2
        if value[1] not in checked:
            checked[value[1]] = []
            rprint("[bold blue]> " + str([value[1]]) +
                   " Passed! [/bold blue]\n")
        else:
            rprint("[red]> Duplicate found: " + str(value[1]) + "[/red]\n")
        # face 3
        if value[2] not in checked:
            checked[value[2]] = []
            rprint("[bold blue]> " + str([value[2]]) +
                   " Passed! [/bold blue]\n")
        else:
            rprint("[red]> Duplicate found: " + str(value[2]) + "[/red]\n")

        distinct_values = set(value)

        for dist_value in distinct_values:
            checked[dist_value].append(value)
        # if the color has exceeded 3 appearances
        rule_broken = False
        if len(checked[value[0]]) > 3:
            rprint("[bold red]" + str([value[0]]) +
                   " appeared more than 3 times.[/bold red]\n")
            rule_broken = True
        if len(checked[value[1]]) > 3:
            rprint("[bold red]" + str([value[1]]) +
                   "  appeared more than 3 times.[/bold red]\n")
            rule_broken = True
        if len(checked[value[2]]) > 3:
            rprint("[bold red]" + str([value[2]]) +
                   "  appeared more than 3 times.[/bold red]\n")
            rule_broken = True
        if (rule_broken == True):
            abides = False
    return abides


if __name__ == '__main__':
    intro()
    # rprint("\n [bold yellow]~~~~~~~~~~~~ PUZZLE 1 ~~~~~~~~~~~~ [/bold yellow]")
    # rules(puzzleOne)
    # rprint("\n [bold yellow]~~~~~~~~~~~~ PUZZLE 2 ~~~~~~~~~~~~ [/bold yellow]")
    # rules(puzzleTwo)
    # rprint("\n [bold yellow]~~~~~~~~~~~~ PUZZLE 3 ~~~~~~~~~~~~ [/bold yellow]")
    # rules(puzzleThree)
    # rprint("\n [bold yellow]~~~~~~~~~~~~ PUZZLE 4 ~~~~~~~~~~~~ [/bold yellow]")
    # rules(puzzleFour)
    # rprint("\n [bold yellow]~~~~~~~~~~~~ PUZZLE 5 ~~~~~~~~~~~~ [/bold yellow]")
    # rules(puzzleFive)
    rprint("\n [bold yellow]~~~~~~~~~~~~ PUZZLE 6 ~~~~~~~~~~~~ [/bold yellow]")
    rules(puzzleSix)
