"""song of eared robot"""
def main():
    """kotoba"""
    text = input().strip()
    count = {}
    order = []
    for ch in text:
        if ch not in count:
            count[ch] = 0
            order.append(ch)
        count[ch] += 1
    result = "".join(ch for ch in order if count[ch] % 2 == 1)
    print(result if result else "fully paired")
main()
