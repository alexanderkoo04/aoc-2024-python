def is_safe(report):
    n = len(report)

    if n < 2:
        return True
    
    direction = 0

    for a, b in zip(report, report[1:]):
        diff = b - a

        if diff == 0 or abs(diff) > 3:
            return False
            
        s = 1 if diff > 0 else -1

        if direction == 0:
            direction = s
        elif direction != s:
            return False 
    
    return True
        
with open('input.txt', 'r') as f:

    safe_cnt = 0

    for line in f:
        report = list(map(int, line.strip().split()))

        if is_safe(report):
            safe_cnt += 1
            continue

        for i in range(len(report)):
            candidate = report[:i] + report[i + 1:]
            if is_safe(candidate):
                safe_cnt += 1
                break
    
    print(safe_cnt)
