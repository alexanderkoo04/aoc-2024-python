with open('input.txt', 'r') as f:

    safe_cnt = 0

    for row in f:
        row = list(map(int, row.strip().split()))
        safe = True
        if row[0] > row[-1]:
            for i in range(len(row) - 1):
                if row[i] <= row[i + 1]:
                    safe = False
                    break
                if abs(row[i] - row[i + 1]) > 3:
                    safe = False
                    break
        elif row[0] < row[-1]:
            for i in range(len(row) - 1):
                if row[i] >= row[i + 1]:
                    safe = False
                    break
                if abs(row[i] - row[i + 1]) > 3:
                    safe = False
                    break
        else:
            safe = False

        if safe:
            safe_cnt += 1
    
    print(safe_cnt)