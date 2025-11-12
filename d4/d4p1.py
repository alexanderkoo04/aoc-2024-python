with open('input.txt', 'r') as f:
    grid = [list(line.strip()) for line in f]
    m = len(grid)
    n = len(grid[0])
    dirs = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

    target = "XMAS"

    sol = 0

    def dfs(x, y, i, ddx, ddy):
        if i == len(target) - 1:
            return 1
        
        curr_score = 0

        if ddx == 0 and ddy == 0:
            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy

                if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == target[i + 1]:
                    curr_score += dfs(nx, ny, i + 1, dx, dy)
        
        else:
            nx = x + ddx
            ny = y + ddy

            if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] == target[i + 1]:
                return dfs(nx, ny, i + 1, ddx, ddy)

        return curr_score

    for x, row in enumerate(grid):
        for y, ch in enumerate(row):
            if ch == 'X':
                sol += dfs(x, y, 0, 0, 0)
    
    print(sol)