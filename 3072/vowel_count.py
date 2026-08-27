"""vowel"""
def main():
    """vowel count"""
    text = input()
    uptxt = text.upper()
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    a +=uptxt.count("A")
    e +=uptxt.count("E")
    i +=uptxt.count("I")
    o +=uptxt.count("O")
    u +=uptxt.count("U")
    if a >0:
        print (f"a : {a}")
    if e >0:
        print (f"e : {e}")
    if i >0:
        print (f"i : {i}")
    if o >0:
        print (f"o : {o}")
    if u >0:
        print (f"u : {u}")
main()
