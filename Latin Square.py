import sys
import math

# Loads the matrix from stdin
def load_matrix():
    return map(int, sys.stdin.read().split())

# Finds the next empty location
def find_zero(m):
    for (i, num) in enumerate(m):
        if num == 0: return i
    return -1

# Finds a possible solution for the matrix at i
def find_num(i, m):
    size = int(math.sqrt(len(m)))
    possibleNumbers = set(range(m[i], size + 1))
    unavaliableNumbers = set(m[i%size:len(m):size]
        + m[i/size*size : i/size*size+size])
    return min(possibleNumbers - unavaliableNumbers or [-1])

# Solves a Latin Square matrix with DFS
def solve_matrix(m):
    stack = []
    i = findZero(m)
    while True:
        if i < 0:
            return m
        nextNum = findNum(i, m)
        if nextNum > 0:
            stack.append((i, m))
            m[i] = nextNum
            i = find_zero(m)
        else:
            m[i] = 0
            i, m = stack.pop()

# Displays matrix in readable form
def print_matrix(m):
    size = int(math.sqrt(len(m)))
    for row in [m[x:x+size] for x in xrange(0, len(m), size)]:
        print(' '.join(map(str, row)))

print_matrix(solve_matrix(load_matrix()))
