"""brick"""
def main():
    """brick"""
    one = int(input())
    five = int(input())
    goal = int(input())
    five *=5
    if five + one< goal or goal%5>one:
        print(-1)
    elif five>goal and not goal%5:
        print(0)
    elif five<goal:
        print(goal-five)
    else:
        print(goal%5)
main()
