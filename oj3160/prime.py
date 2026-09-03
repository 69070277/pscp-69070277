"""prime"""
def main():
    """prime number"""
    st,end = map(int,input().split())
    prime = []
    for num in range(max(st, 2), end + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if not num % i:
                is_prime = False
                break
        if is_prime:
            prime.append(num)
    if len(prime) >= 1:
        print(' '.join(map(str, prime)))
    print(f"Total primes: {len(prime)}")
main()
