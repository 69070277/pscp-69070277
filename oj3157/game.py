"""lab"""
def main():
    """lab"""
    r = int(input())
    total = 0
    for _ in range(r):
        symble = input()
        if symble=="+":
            total+=10
        else:
            total-=5
    print(total)
main()
