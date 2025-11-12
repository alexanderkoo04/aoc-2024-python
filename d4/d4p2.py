with open('input.txt', 'r') as f:
    grid = [list(line.strip()) for line in f]

    m = len(grid)
    n = len(grid[0])

    sol = 0

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            if grid[i][j] == 'A':
                
                d1 = grid[i - 1][j - 1] + grid[i + 1][j + 1]
                d2 = grid[i + 1][j - 1] + grid[i - 1][j + 1]

                if d1 in ("MS", "SM") and d2 in ("MS", "SM"):
                    sol += 1
    
    print(sol)