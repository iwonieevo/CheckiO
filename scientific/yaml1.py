def yaml(a: str) -> dict:
    yaml_dict = {}
    for elem in a.split("\n"):
        if ":" not in elem:
            continue
        if elem.replace(" ", "", 1).split(":")[1].isdigit():
            yaml_dict[elem.replace(" ", "", 1).split(":")[0]] = int(elem.replace(" ", "", 1).split(":")[1])
        else:
            yaml_dict[elem.replace(" ", "", 1).split(":")[0]] = elem.replace(" ", "", 1).split(":")[1]
    return yaml_dict


assert yaml("name: Alex\nage: 12") == {"name": "Alex", "age": 12}
assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {
    "age": 12,
    "name": "Alex Fox",
    "class": "12b",
}

print("The mission is done! Click 'Check Solution' to earn rewards!")
