"""temperature"""
def main():
    """main"""
    tem = float(input())
    fst = input()
    snd = input()
    C=0
    if fst.upper() == "C":
        C = tem
    elif fst.upper() == "K":
        C = tem-273.15
    elif fst.upper() == "F":
        C = (tem-32)*5/9
    elif fst.upper() == "R":
        C = tem*5/9-273.15
    K = C+273.15
    F = C*9/5+32
    R = K*9/5
    if snd.upper() == "C":
        print(f"{C:.2f}")
    elif snd.upper() == "K":
        print(f"{K:.2f}")
    elif snd.upper() == "F":
        print(f"{F:.2f}")
    elif snd.upper() == "R":
        print(f"{R:.2f}")
main()
