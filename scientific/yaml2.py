def yaml(a: str) -> dict:
    yaml_dict = {}
    for elem in a.split("\n"):
        if ":" not in elem:
            continue
        fixed_elem = elem.replace("\\", "").split(":")
        fixed_elem[1] = fixed_elem[1].strip()
        if fixed_elem[1] == "" or fixed_elem[1].upper() == "NULL":
            yaml_dict[fixed_elem[0]] = None
            continue
        if len(fixed_elem[1]) > 1:
            if (fixed_elem[1][0] == '"' and fixed_elem[1][-1] == '"') or (fixed_elem[1][0] == "'" and fixed_elem[1][-1] == "'"):
                fixed_elem[1] = fixed_elem[1][1:-1]
        if fixed_elem[1].isdigit():
            yaml_dict[fixed_elem[0]] = int(fixed_elem[1])
        elif fixed_elem[1].upper() == "TRUE":
            yaml_dict[fixed_elem[0]] = True
        elif fixed_elem[1].upper() == "FALSE":
            yaml_dict[fixed_elem[0]] = False
        else:
            yaml_dict[fixed_elem[0]] = fixed_elem[1]
    return yaml_dict


assert yaml("name: Alex\nage: 12") == {"name": "Alex", "age": 12}
assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {
    "name": "Alex Fox",
    "age": 12,
    "class": "12b",
}
assert yaml('name: "Alex Fox"\nage: 12\n\nclass: 12b') == {
    "name": "Alex Fox",
    "age": 12,
    "class": "12b",
}
assert yaml('name: "Alex \\"Fox\\""\nage: 12\n\nclass: 12b') == {
    "name": 'Alex "Fox"',
    "age": 12,
    "class": "12b",
}
assert yaml('name: "Bob Dylan"\nchildren: 6\nalive: false') == {
    "name": "Bob Dylan",
    "children": 6,
    "alive": False,
}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding:') == {
    "name": "Bob Dylan",
    "children": 6,
    "coding": None,
}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding: null') == {
    "name": "Bob Dylan",
    "children": 6,
    "coding": None,
}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding: "null" ') == {
    "name": "Bob Dylan",
    "children": 6,
    "coding": "null",
}

print("The mission is done! Click 'Check Solution' to earn rewards!")
