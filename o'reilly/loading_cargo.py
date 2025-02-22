from itertools import combinations


def checkio(data):
    best_diff = max(data)   # our return value, by definition, the smallest difference between the sets can't be greater than the biggest value in the data
    for _ in range(int(len(data)/2) + 1):   # we temporarily make ALL possible sets (since we are only creating 1 of 2 sets, because we can define the other set, by the first one, our sets will have length from 1 to size of data/2 + 1
        possible_sets = combinations(data, _)
        for combination in possible_sets:   # then we check for the weight differences in all sets, we store the lowest one
            if abs(sum(data) - sum(combination) * 2) < best_diff:
                best_diff = abs(sum(data) - sum(combination) * 2)   # summed weights from second set = all weights summed - sum of weights in the first set
    return best_diff


if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"
