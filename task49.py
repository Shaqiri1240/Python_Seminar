import math

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
def find_farthest_orbit(orbits):
    max_area = 0
    max_ind = 0
    for i in range(len(orbits)):
        if orbits[i][0] != orbits[i][1]:
            S = math.pi * orbits[i][0] * orbits[i][1]

            if S >= max_area :
                max_ind = i
                max_area = S
    return orbits[max_ind]
print(*find_farthest_orbit(orbits))