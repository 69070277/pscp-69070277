"""trick heart"""
def main():
    """MIMI"""
    n, s = map(int, input().split())
    nxt = [0] * (n + 1)
    for i in range(1, n + 1):
        nxt[i] = int(input())
    visited = [False] * (n + 1)
    count = 0
    while s and not visited[s]:
        visited[s] = True
        count += 1
        s = nxt[s]
    print(count)
main()
