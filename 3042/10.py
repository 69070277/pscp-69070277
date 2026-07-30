"""10"""
def main():
    """main"""
    num = int(input())
    num -= num%10
    rs = str(num)
    while num>0:
        num-=10
        rs += (f" {str(num)}")
    print(rs)
main()
