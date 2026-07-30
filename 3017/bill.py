"""Bill"""
num = int(input())
ser = num*(10/100)
if ser <= 50 :
    rs = (num+50)*(107/100)
    print(f"{rs:.2f}")
elif ser>= 1000:
    rs = (num+1000)*(107/100)
    print(f"{rs:.2f}")
else :
    rs = (num+ser)*(107/100)
    print(f"{rs:.2f}")
