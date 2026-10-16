"""untie it gently"""
def main():
    """yura yurari"""
    n = int(input())
    cats = {}
    foxes = {}
    for _ in range(n):
        line = input().strip()
        line = line.replace("{", "").replace("}", "")
        parts = line.split(":")
        name = parts[0].strip().strip('"')
        code = parts[1].strip().strip('"')
        num = int(code[3:])
        if code.startswith("Cat"):
            cats[num] = name
        else:
            foxes[num] = name
    used_names = list(cats.values()) + list(foxes.values())
    if 1 not in cats and "Garfield" not in used_names:
        cats[1] = "Garfield"
    if 1 not in foxes and "Fubuki" not in used_names:
        foxes[1] = "Fubuki"
    print("Cat :", len(cats))
    print("Fox :", len(foxes))
    for num in sorted(cats):
        print(cats[num], ": Cat" + str(num).zfill(2))
    for num in sorted(foxes):
        print(foxes[num], ": Fox" + str(num).zfill(2))
main()
