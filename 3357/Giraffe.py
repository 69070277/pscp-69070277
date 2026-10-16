"""Human"""
def main():
    """Masquerading"""
    am = int(input())
    lst = [0]
    for _ in range(am):
        h = int(input())
        lst.append(h)
    lst.append(0)
    rs = 0
    for i in range(1,am+1):
        if lst[i]>lst[i-1] and lst[i]>lst[i+1]:
            rs+=1
    print(rs)
main()
