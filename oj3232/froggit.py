"""ribbit"""
def main():
    """jump"""
    start,goal = map(int,input().split())
    cnt = 0
    mix = 0
    while True:
        if mix >= goal:
            break
        if start<=0:
            cnt =-1
            break
        mix += start
        start-=2
        cnt+=1
    print(cnt)
main()
