"""war"""
def main():
    """war"""
    st,fn = map(str, input().split())
    w = float(input())
    fst = 0
    wkg = 0
    if st == "BKK":
        if fn == "CNX":
            fst =10
            wkg = 30
        elif fn == "PKT":
            fst =25
            wkg = 50
    elif st == "CNX" and fn == "UBP":
        fst =15
        wkg = 40
    elif st == "UBP":
        if fn == "BKK":
            fst = 20
            wkg = 40
        elif fn == "PKT":
            fst =40
            wkg = 70
    elif st =="PKT" and fn == "CNX":
        fst = 30
        wkg = 60
    rs =fst+wkg*w
    if not fst:
        print("Error")
    else:
        print(f"{rs:.2f}")
main()
