"""store"""
def main():
    """check"""
    num,check = map(int,input().split())
    dicstart = []
    dicstop = []
    rs = ""
    for _ in range(num):
        start,stop = map(int,input().split())
        dicstart.append(start)
        dicstop.append(stop)
    x = input()
    time = [int(t) for t in x.split()]
    for i in range(check):
        count = 0
        for y in range(num):
            if dicstart[y]<=time[i] and dicstop[y]>time[i]:
                count+=1
        if i!=check-1:
            rs +=f"{str(count)} "
        else:
            rs +=f"{str(count)}"
    print(rs)
main()
