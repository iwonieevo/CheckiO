from itertools import combinations


def unix_match(filename: str, pattern: str) -> bool:
    for piece in pattern.split('*'):
        if piece not in filename:
            flag = False
            for combination in combinations(list(filename), piece.count('?')):
                temp = piece
                for char in combination:
                    temp = temp.replace('?', char, 1)
                if temp in filename:
                    flag = True
                    break
            if not flag:
                return False
    return True


print("Example:")
print(unix_match("somefile.txt", "*.*"))

assert unix_match("somefile.txt", "*") is True
assert unix_match("other.exe", "*") is True
assert unix_match("my.exe", "*.txt") is False
assert unix_match("log1.txt", "log?.txt") is True
assert unix_match("log12.txt", "log?.txt") is False
assert unix_match("log12.txt", "log??.txt") is True

print("The mission is done! Click 'Check Solution' to earn rewards!")
