"""lab"""
def main():
    """lab"""
    l,n = map(int,input().split())
    j=l
    anw = 1
    mul=0
    base = 0
    while True:
        if not j:
            break
        base+=j
        j-=1
    total=base
    while True:
        if total>=n:
            break
        mul+=l
        total+=mul*l+base
        anw+=1
    print(anw)
main()
