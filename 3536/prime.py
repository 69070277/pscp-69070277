"""buriki no dance"""
def main():
    """Eguri nuita kodou sakase sakase"""
    n = int(input())
    if n < 2:
        print("NO")
        return
    if n < 4:
        print("YES")
        return
    if not n % 2:
        print("NO")
        return
    limit = int(n ** 0.5)
    d = 3
    while d <= limit:
        if not n % d:
            print("NO")
            return
        d += 2
    print("YES")
main()
