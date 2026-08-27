"""shop"""
def main():
    """SHOP"""
    mem = input()
    am = int(input())
    total = 0
    for _ in range(am):
        price = float(input())
        total+=price
    if mem == "Y":
        total-=total*5/100
    elif mem == "N" and total>=500:
        total-=total*3/100
    if total>round(total,2):
        total+=0.01
    print(f"{total:.2f}")
main()
