"""clover"""
def main():
    """the brush the paint it all in it position"""
    m = int(input())
    n = int(input())
    ml = []
    anw = []
    for _ in range(m):
        sm = int(input())
        ml.append(sm)
    for _ in range(n):
        sn = int(input())
        if sn in ml:
            anw.append(sn)
    if not anw:
        print("Nope")
    else:
        anw.sort(reverse=True)
        for i in anw:
            print(i)
main()
