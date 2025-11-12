import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

with open('input.txt', 'r') as f:

    text = f.read()

    pairs = [(int(a), int(b)) for a, b in re.findall(pattern, text)]

    sol = 0

    for a, b in pairs:
        sol += a * b
    
    print(sol)
