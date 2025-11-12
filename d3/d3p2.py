import re

pattern = r"(mul)\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"

with open('input.txt', 'r') as f:

    text = f.read()

    valid = re.findall(pattern, text)

    sol = 0
    on = True

    for query in valid:
        if not on:
            if not query[3]:
                continue
            on = True
        else:
            if query[0]:
                sol += int(query[1]) * int(query[2])
            elif query[4]:
                on = False

    print(sol)
