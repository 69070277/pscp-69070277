"""gordon"""
def main():
    """this is not a padthai at all"""
    recipe = {"Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
              "Bean Sprouts", "Noodle", "Chives", "Lime",
              "Egg", "Oil", "Peanuts"}
    good_taste = {"Sweet", "Sour", "Salty"}
    used = set()
    item = input().strip()
    while item != "Cook":
        used.add(item)
        item = input().strip()
    tastes = set()
    t = input().strip()
    while t != "End":
        tastes.add(t)
        t = input().strip()
    if used - recipe:
        print("This is not Pad Thai!!!")
    elif used != recipe:
        print("This is bad!")
    elif tastes != good_taste:
        print("Not Bad...")
    else:
        print("Delicious!")
main()
