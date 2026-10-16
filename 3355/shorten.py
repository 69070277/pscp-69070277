"""rejected diva"""
def main():
    """uta hime"""
    lst = []
    cnt = 0
    stl = ""
    anw = ""
    while True:
        num = int(input())
        if num == -1:
            break
        lst.append(num)
    lst.sort()
    if len(lst)>0:
        anw = f"{lst[0]}"
        last = lst[0]
        for i in lst:
            if i==lst[0]:
                continue
            if i== last+1:
                anw += "-"
            elif i!=last+1 and anw[-1]=="-":
                anw+=f"{str(last)}, {str(i)}"
            elif i!=last+1:
                anw+=f", {str(i)}"
            last = i
        for i in anw:
            cnt+=1
            if i =="-" and stl == "-":
                anw=anw[:cnt-1]+anw[cnt:]
                cnt-=1
            stl=i
        if anw[-1]=="-":
            anw+=f"{last}"
    print(anw)
main()
