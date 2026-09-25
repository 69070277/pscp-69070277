"""rgb"""
import math
def main():
    """rgb"""
    r1,g1,b1 = map(int,input().split())
    r2,g2,b2 = map(int,input().split())
    r = str(math.floor((r1+r2)/2))
    g = str(math.floor((g1+g2)/2))
    b = str(math.floor((b1+b2)/2))
    print(f"{r} {g} {b}")
main()
