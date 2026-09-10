"""gacha time"""
def main():
    """Kuu ni naru"""
    alp1,num1 = map(str,input().split())
    alp2,num2 = map(str,input().split())
    if alp1 == alp2:
        if num1 == num2:
            print(1000000)
        elif num1[2:] == num2[2:]:
            print(2000)
        elif num1[3:] == num2[3:]:
            print(1000)
        else:
            print(20)
    else:
        if num1 == num2:
            print(100000)
        elif num1[2:] == num2[2:]:
            print(200)
        elif num1[3:] == num2[3:]:
            print(100)
        else:
            print(0)
main()
