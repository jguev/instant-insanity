from math import floor, pi, e
from typing import List, Dict

# Triangular prism, 3 faces
f1: List[int] = []
f2: List[int] = []
f3: List[int] = []

# Puzzles required from assignment, 6
puzzleOne: List[List[int]] = []
puzzleTwo: List[List[int]] = []
puzzleThree: List[List[int]] = []
puzzleFour: List[List[int]] = []
puzzleFive: List[List[int]] = []
puzzleSix: List[List[int]] = []

# Counting occurrences
occurrencesCounter: Dict[int, List[List[int]]]

# Generate Data
# Puzzle 1: 1 + ((floor n * 17 pi^6)mod 31) ~ 1 + ((floor(n * (17 * pow(pi, 6)))) % 31)
# Puzzle 2: 1 + ((floor n * 17 e^6)mod 31) ~ 1 + ((floor(n * (17 * pow(e, 6)))) % 31)
# Puzzle 3: 1 + ((floor n * 17 e^8)mod 31) ~ 1 + ((floor(n * (17 * pow(e, 8)))) % 31)
# Puzzle 4: 1 + ((floor n * 11 e^8)mod 31) ~ 1 + ((floor(n * (11 * pow(e, 8)))) % 31)
# Puzzle 5: 1 + ((floor n * 101 e^2)mod 31) ~ 1 + ((floor(n * (101 * pow(e, 2)))) % 31)
# Puzzle 6: 1 + ((floor n * 101 e^8)mod 31) ~ 1 + ((floor(n * (101 * pow(e, 8)))) % 31)
for n in range(1, 93, 5):
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


# Fancy logic belongs here
print(puzzleOne)
print(puzzleTwo)
print(puzzleThree)
print(puzzleFour)
print(puzzleFive)
print(puzzleSix)
