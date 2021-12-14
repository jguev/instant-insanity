from rich import print as rprint
from math import floor, pi, e
from typing import List, Dict

# Known:
# Triangular prism, 3 faces
# Colors are assigned counter-clockwise: f1 > f2 > f3
# Six puzzles with predefined formulas

# FACES
f1: List[int] = []  # front
# for the purposes of rotation reference f1 is assumed to always be the front/pivot/etc.
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
    rprint("[blue]Generating colors with the given constraints ...[/blue]")

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
               ": " + f[p_number-1] + "[/bold green]\n")

        # prints colors [ color of face 1, color of face 2, color of face 3]
        print(p[p_number-1])

        rprint("\n[bold blue]Before rotations: [/bold blue]")
        if (rules(i) == True):
            rprint("[blue]Solution[/blue]\n")
        else:
            rprint("[blue]No solution.[/blue]\n")
            rebuildTower(i, p_number)


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

########################   RULES   ########################


def rules(puzzle: List[List[int]]) -> bool:
    checked = {}
    counter = 0
    # set the puzzle as rule abiding (true) until proven otherwise
    abides: bool = True
    for value in puzzle:
        counter = counter+1
        # rprint("[bold blue]\n\nChecking slice " +
        #        str(counter) + "... [/bold blue]\n")
        # if (face 1) is a unique color place in checked
        if value[0] not in checked:
            checked[value[0]] = []
        #     rprint("[bold blue]> " + str([value[0]]) +
        #            " Passed! [/bold blue]\n")
        # else:
        #     rprint("[red]> Duplicate found: " + str(value[0]) + "[/red]\n")
        # face 2
        if value[1] not in checked:
            checked[value[1]] = []
        #     rprint("[bold blue]> " + str([value[1]]) +
        #            " Passed! [/bold blue]\n")
        # else:
        #     rprint("[red]> Duplicate found: " + str(value[1]) + "[/red]\n")
        # face 3
        if value[2] not in checked:
            checked[value[2]] = []
        #     rprint("[bold blue]> " + str([value[2]]) +
        #            " Passed! [/bold blue]\n")
        # else:
        #     rprint("[red]> Duplicate found: " + str(value[2]) + "[/red]\n")

        unique = set(value)

        for dist_value in unique:
            checked[dist_value].append(value)
        # if the color has exceeded 3 appearances
        rule_broken = False
        if len(checked[value[0]]) > 3:
            # rprint("[bold red]" + str([value[0]]) +
            #        " appeared more than 3 times.[/bold red]\n")
            rule_broken = True
        if len(checked[value[1]]) > 3:
            # rprint("[bold red]" + str([value[1]]) +
            #        "  appeared more than 3 times.[/bold red]\n")
            rule_broken = True
        if len(checked[value[2]]) > 3:
            # rprint("[bold red]" + str([value[2]]) +
            #        "  appeared more than 3 times.[/bold red]\n")
            rule_broken = True
        if (rule_broken == True):
            abides = False
    return abides

########################   FACES  ########################


def faces(curr: int):
    while len(f1) > curr:
        f1.pop()
        f2.pop()
        f3.pop()

########################   TRANSFER  ########################
# Handle inserting the values into their new positions


def transfer(curr: int, side: int, puzzle: List[List[int]]) -> bool:
    faces(curr)

    if puzzle[curr][side % 3] in f1:
        return False
    if puzzle[curr][(side + 1) % 3] in f2:
        return False
    if puzzle[curr][(side + 2) % 3] in f3:
        return False

    if curr >= len(f1):
        f1.insert(curr, puzzle[curr][side % 3])
        f2.insert(curr, puzzle[curr][(side + 1) % 3])
        f3.insert(curr, puzzle[curr][(side + 2) % 3])
    else:
        f1[curr] = puzzle[curr][side % 3]
        f2[curr] = puzzle[curr][(side + 1) % 3]
        f3[curr] = puzzle[curr][(side + 2) % 3]

    return True

########################   ROTATE  ########################
#  Values will change within but variable names remain consistent.
#  Face 1 will always face forward ...
#   [f1] - [f2] - [f3]
#   [f3] - [f1] - [f2]
#   [f2] - [f3] - [f1]
#   back to start


def rotate(curr: int, puzzle: List[List[int]]) -> bool:
    if curr == len(puzzle):
        return True
    else:
        # (1) 2 3
        #  1 (2) 3
        if transfer(curr, 0, puzzle):
            if rotate(curr + 1, puzzle):
                return True
        #  1 (2) 3
        #  1  2 (3)
        if transfer(curr, 1, puzzle):
            if rotate(curr + 1, puzzle):
                return True
        #  1 2 (3)
        # (1) 2 3
        if transfer(curr, 2, puzzle):
            if rotate(curr + 1, puzzle):
                return True
    # False: Solution does not exist
        return False

########################   REBUILD TOWER   ########################
# Input: Tower > No Solution
# During: Through rotation, a new tower will be rebuilt with a solution
# Output: 1) Tower > Solution or 2) Tower > Minimum Obstacles


def rebuildTower(puzzle: List[List[int]], p_number: int):
    global implementation
    if (rules(puzzle) == False):
        rprint("[bold blue]After rotations: [/bold blue]")
        if rotate(0, puzzle):
            # Tower > Solution
            rprint("[blue]Solution found.[/blue]")
            print(f1)
            print(f2)
            print(f3)
        else:
            # Tower > Minimum Obstacles
            rprint("[blue]No solution. \nNeed to look for minimum obstacles.[/blue]")


if __name__ == '__main__':
    intro()
