import csv
import heapq

with open('input.csv', newline='') as f:
    values = csv.reader(f, delimiter=',')
    
    left_list = []
    right_list = []

    for row in values:
        left, right = map(int, row)
        heapq.heappush(left_list, left)
        heapq.heappush(right_list, right)
    
    sum_diff = 0

    while left_list:
        sum_diff += abs(heapq.heappop(left_list) - heapq.heappop(right_list))

    print(sum_diff)