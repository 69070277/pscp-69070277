"""You know im bad"""
def main():
    """dakinai"""
    n,k,t = map(int, input().split())
    ppl = 1
    count = 1
    if ppl == t:
        print(count)
        return
    for _ in range(n):
        ppl = (ppl - 1 + k) % n + 1
        if ppl == 1:
            break
        count += 1
        if ppl == t:
            break
    print(count)
main()
