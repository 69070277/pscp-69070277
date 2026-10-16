"""Water the Roses"""
def main():
    """cause it feel so stupid cause you feel the same"""
    w, h, m, n = map(int, input().split())
    xs = [0] + list(map(int, input().split())) + [w]
    ys = [0] + list(map(int, input().split())) + [h]

    widths = sorted([xs[i + 1] - xs[i] for i in range(len(xs) - 1)], reverse=True)
    heights = sorted([ys[i + 1] - ys[i] for i in range(len(ys) - 1)], reverse=True)

    first = widths[0] * heights[0]
    second = max(widths[0] * heights[1], widths[1] * heights[0])
    print(first, second)
    while True:
        if m>=0 or n>=0:
            break
        print("what")
main()
