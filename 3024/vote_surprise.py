"""Vote"""
def main():
    """main"""
    total = float(input())
    most = float(input())
    low = total-most*2
    if low<0:
        low = 0
    if most-low > 2:
        print("Surprising")
    else :
        print("Not surprising")
main()
