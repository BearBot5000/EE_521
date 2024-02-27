import random


def shor_find_order_classical(a: int, product: int) -> int:
    exp = 1
    for r in range(1, product):
        exp *= a
        exp %= product
        if exp == 1:
            return r
    raise "Shor Classical Failed"


def shor_find_factor(product):
    # https://en.wikipedia.org/wiki/Shor%27s_algorithm
    if product % 2 == 0:
        return 2
    while True:
        # Pick a random number 1 < a < N {\displaystyle 1<a<N}.
        a = random.randrange(2, product - 1)
        print(f"Trying shor again, a={a}")
        K = gcd(a, product)
        if K != 1:
            return K
        # print(f"K is {K}")
        r = shor_find_order_classical(a, product)
        # print(f"R is {r}")
        # If r {\displaystyle r} is odd, then go back to step 1.
        if r % 2 == 1:
            # print("R is odd")
            continue
        # Compute g = gcd ( N , a r / 2 + 1 ) {\displaystyle g=\gcd(N,a^{r/2}+1)}. If g {\displaystyle g} is nontrivial, the other factor is N g {\textstyle {\frac {N}{g}}}, and we're done. Otherwise, go back to step 1.
        g = gcd(product, a ^ int(r / 2) + 1)
        # print(f"g is {g}")
        # Is g trivial
        if g == 1 or g == product:
            # print("g is so trivial")
            continue
        return g


def gcd(a: int, b: int) -> int:
    while a != 0:
        c = a
        a = b % a
        b = c
    return b


def find_factor(product: int) -> int:
    """
    :param product:
    :return: A factor of param, or -1 if prime
    """
    if product < 2:
        raise ":("

    for a in range(2, product):
        for b in range(a, product):
            if a * b == product:
                return a
    return -1


if __name__ == '__main__':
    find = 227119 # 49414657
    print(f"A factor is {find_factor(find)}")
    print(f"GCD is {gcd(116158341, 2009136727)}")
    print(f"shors {shor_find_factor(find)}")

