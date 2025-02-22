from typing import List, Tuple
from math import sqrt
Coords = List[Tuple[int, int]]


def similar_triangles(t1: Coords, t2: Coords) -> bool:
    t1_sides = sorted([sqrt((t1[0][0] - t1[1][0])**2 + (t1[0][1] - t1[1][1])**2), sqrt((t1[1][0] - t1[2][0])**2 + (t1[1][1] - t1[2][1])**2), sqrt((t1[2][0] - t1[0][0])**2 + (t1[2][1] - t1[0][1])**2)])
    t2_sides = sorted([sqrt((t2[0][0] - t2[1][0])**2 + (t2[0][1] - t2[1][1])**2), sqrt((t2[1][0] - t2[2][0])**2 + (t2[1][1] - t2[2][1])**2), sqrt((t2[2][0] - t2[0][0])**2 + (t2[2][1] - t2[0][1])**2)])
    if t1_sides[0]/t2_sides[0] == t1_sides[1]/t2_sides[1] == t1_sides[2]/t2_sides[2]:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")
