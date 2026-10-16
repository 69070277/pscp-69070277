"""right away my master"""
def main():
    """Inochi ni Kirawarete"""
    n, p = input().split()
    n = int(n)
    p = float(p)
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))
    col_tiles = [0] * n
    col_points = [0] * n
    total_tiles = 0
    total_points = 0
    for i in range(n):
        row_tiles = 0
        row_points = 0
        for j in range(n):
            x = grid[i][j]
            if x > 0:
                row_tiles += 1
                col_tiles[j] += 1
            row_points += x
            col_points[j] += x
        print(" ".join(map(str, grid[i])), row_tiles, row_points)
        total_tiles += row_tiles
        total_points += row_points
    print(" ".join(map(str, col_tiles)))
    print(" ".join(map(str, col_points)))
    print(total_tiles, total_points, f"{total_points * p:.2f}")
main()
