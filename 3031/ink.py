"""ink"""
def main():
    """tokyo teddy bear"""
    pi = 3.1416
    info = input()
    info_dic = [int(x) for x in info.split()]
    sp = info_dic[0]
    pp = info_dic[1]
    for _ in range(pp):
        xy = input()
        xy_dic = [int(y) for y in xy.split()]
        x = xy_dic[0]
        y = xy_dic[1]
        r = (x**2+y**2)**0.5
        less_ar = pi*r**2
        rs = less_ar/sp
        if round(rs) > rs:
            rs = round(rs)
        elif round(rs) < rs:
            rs = round(rs)+1
        print(round(rs))
main()
