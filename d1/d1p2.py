import csv
from collections import defaultdict

with open('input.csv', 'r', newline='') as f:
    values = csv.reader(f, delimiter=',')

    left_freq = defaultdict(int)
    right_freq = defaultdict(int)

    for row in values:
        left, right = map(int, row)
        print(left, end=' ')
        print(right)
        left_freq[left] += 1
        right_freq[right] += 1
    
    sim_score = 0

    for key, value in left_freq.items():
        sim_score += key * value * right_freq[key]
    
    print(sim_score)