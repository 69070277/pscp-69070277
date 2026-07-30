"""Castle"""
def main():
    """main"""
    room = int(input())
    info = room
    while True:
        if info**0.5 == round(info**0.5):
            break
        info +=1
    floor = round(info**0.5)
    if floor%2 and room%2 == 1 or not floor%2 and not room%2:
        rs = (floor-1)*2
    else :
        rs = 1+(floor-2)*2
    print(rs)
main()
