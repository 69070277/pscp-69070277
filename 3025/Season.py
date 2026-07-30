"""Season"""
def main():
    """WONDERHOY"""
    month = int(input())
    day = int(input())
    season = ["winter", "spring", "summer", "fall"]
    x=0
    if 1 <= month <= 3:
        x = 0
    elif 4 <= month <= 6:
        x = 1
    elif 7 <= month <= 9:
        x = 2
    elif 10 <= month <= 12:
        x = 3
    if not month%3 and day >=21:
        x += 1
        if x == 4:
            x = 0
    print(season[x])
main()
