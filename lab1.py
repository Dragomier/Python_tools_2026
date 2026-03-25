# Ex. 1
import sys


def print_hello():
    print("Hello World")

# Ex. 2
import math
def quadratic():
    a = int(input("Give the quadratic term: "))
    b = int(input("Give the linear term: "))
    c = int(input("Give the free term: "))
    disc = b ** 2 - 4 * a * c
    if disc < 0:
        print("No solutions")
    elif disc == 0:
        print("Solution: " + str(-b/(2 * a)))
    else:
        x_1 = (-1 * b - math.sqrt(disc))/(2 * a)
        x_2 = (-1 * b + math.sqrt(disc))/(2 * a)
        print(f"Solutions: {x_1, x_2}")

# Ex. 3
import sys
def print_parameters():
    for index, arg in enumerate(sys.argv[1:]):
        print(index + 1, arg)

# Ex. 4
import math
import random
def Monte_Carlo():
    how_many_iterations = int(input("Give the number of iterations: "))
    step = int(input("Give the display step: "))
    numbers = [[random.random(), random.random()] for i in range(how_many_iterations)]
    points = [numbers[i][0] * numbers[i][0] + numbers[i][1] * numbers[i][1]  <= 1 for i in range(how_many_iterations)]
    print(sum([True, True]))
    for i in range(1, how_many_iterations//step + 1):
        print("Przybliżenie pi po " + str(i*step) + " krokach: " + str(4 * sum(points[0: step * i])/ (i * step)))
    print("Właściwa liczba pi: " + str(math.pi))
Monte_Carlo()





