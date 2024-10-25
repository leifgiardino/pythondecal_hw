import numpy as np

# Q 1
arr = np.array([[1, 2, 3], [5, 7, 9], [2, 4, 6], [7, 7, 7]])
def onlyOdd(arr):
    odd_rows = [row for row in arr if np.all(row % 2 != 0)]
    return np.array(odd_rows)
onlyOdds = onlyOdd(arr)
print(onlyOdds)

# Q 2.1
checkerboardpt1 = np.zeros((8,8))
print(checkerboardpt1)

# Q 2.2
def alternateOdd(checkerboardpt1):
    checkerboardpt1[::2, ::2] = 1
    return checkerboardpt1
checkerboardpt2 = alternateOdd(checkerboardpt1)
print(checkerboardpt2)

# Q 2.3
def alternateEven(checkerboardpt2):
    checkerboardpt2[1::2, 1::2] = 1
    return checkerboardpt1
checkerboard = alternateEven(checkerboardpt2)
print(checkerboardpt2)

# Q 2.4
reversed_checkerboard = np.flip(checkerboard, axis=0)
print(reversed_checkerboard)

# Q 3
universe = np.array(['galaxy', 'cluster'])
def expansion(universe, num_spaces):
    space = ' ' * num_spaces
    return np.char.join(space, universe)
print(expansion(universe, 1))
print(expansion(universe, 2))

# Q 4
np.random.seed(42)
planets = np.random.randint(100, 1000, (5, 5))
def seconLargest(planets):
    sort_descending = np.sort(planets, axis=0)[::-1]
    return sort_descending[1]
secondBiggest = seconLargest(planets)
print(secondBiggest)