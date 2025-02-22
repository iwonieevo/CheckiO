def identify_block(numbers):
    letters = {
        (0, 4, 8, 12): 'I',
        (1, 5, 8, 9): 'J',
        (0, 4, 8, 9): 'L',
        (0, 1, 4, 5): 'O',
        (1, 2, 4, 5): 'S',
        (0, 1, 2, 5): 'T',
        (0, 1, 5, 6): 'Z'
    }

    def normalize(b):
        m = (min(b) // 4) * 4 + min(x % 4 for x in b)
        return tuple(x - m for x in sorted(b))

    numbers = normalize([x - 1 for x in numbers])
    for block, letter in letters.items():
        grid = [1 if i in block else 0 for i in range(16)]
        grid = tuple(tuple(grid[i:i + 4]) for i in range(0, 16, 4))
        for i in range(4):
            g = sum(grid, ())
            if numbers == normalize([i for i in range(16) if g[i]]):
                return letter
            grid = tuple([r for r in zip(*grid)][::-1])


if __name__ == '__main__':
    assert identify_block({10, 13, 14, 15}) == 'T', 'T'
    assert identify_block({1, 5, 9, 6}) == 'T', 'T'
    assert identify_block({2, 3, 7, 11}) == 'L', 'L'
    assert identify_block({4, 8, 12, 16}) == 'I', 'I'
    assert identify_block({3, 1, 5, 8}) is None, 'None'
    print('"Run" is good. How is "Check"?')
