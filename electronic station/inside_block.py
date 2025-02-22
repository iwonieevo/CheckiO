from sympy import Polygon


def is_inside(polygon: list[tuple[int, int]], point: tuple[int, int]) -> bool:
    poly = Polygon(*polygon)
    return poly.encloses_point(point) or any(point in side for side in poly.sides)


# These "asserts" are used for self-checking
assert is_inside([(1, 1), (1, 3), (3, 3), (3, 1)], (2, 2)) == True
assert is_inside([(1, 1), (1, 3), (3, 3), (3, 1)], (4, 2)) == False
assert is_inside([(1, 1), (4, 1), (2, 3)], (3, 2)) == True
assert is_inside([(1, 1), (4, 1), (1, 3)], (3, 3)) == False
assert is_inside([(2, 1), (4, 1), (5, 3), (3, 4), (1, 3)], (4, 3)) == True
assert is_inside([(2, 1), (4, 1), (3, 2), (3, 4), (1, 3)], (4, 3)) == False
assert (
        is_inside([(1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)], (3, 3)) == True
)
assert (
        is_inside([(1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)], (4, 3))
        == False
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
