"""color"""
frs = input()
snd = input()
if frs == "Red":
    if snd == "Red":
        print("Red")
    elif snd == "Yellow":
        print("Orange")
    elif snd == "Blue":
        print("Violet")
    else:
        print("Error")
elif frs == "Yellow":
    if snd == "Red":
        print("Orange")
    elif snd == "Yellow":
        print("Yellow")
    elif snd == "Blue":
        print("Green")
    else:
        print("Error")
elif frs == "Blue":
    if snd == "Red":
        print("Violet")
    elif snd == "Yellow":
        print("Green")
    elif snd == "Blue":
        print("Blue")
    else:
        print("Error")
else :
    print("Error")
