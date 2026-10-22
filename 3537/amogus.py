"""moongus"""
def main():
    """oninoinumani"""
    alive = {}
    dead = {}
    line = input().strip()
    while line != "Start":
        parts = line.replace("'", '"').split('"')
        alive[parts[1]] = parts[3]
        line = input().strip()
    line = input().strip()
    while line != "End":
        if line in alive:
            dead[line] = alive.pop(line)
        line = input().strip()
    print(list(alive.values()).count("Impostor"), "Impostor Remains")
    print("***Alive***")
    for name in sorted(alive):
        print(name, ":", alive[name])
    print("***Dead***")
    for name in sorted(dead):
        print(name, ":", dead[name])
main()
