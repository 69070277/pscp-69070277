"""cards"""
def main():
    """pot of greed"""
    text = input().upper()
    x=1
    if text[0] == "1":
        x+=1
        rank = "10"
    elif text[0] == "A":
        rank = "ace"
    elif text[0] == "Q":
        rank = "queen"
    elif text[0] == "J":
        rank = "jack"
    elif text[0] == "K":
        rank = "king"
    else:
        rank = f"{str(text[0])}"

    if text[x] == "D":
        group = "diamonds"
    elif text[x] == "H":
        group = "hearts"
    elif text[x] == "S":
        group = "spades"
    else:
        group = "clubs"
    print(f"{rank} of {group}")
main()
