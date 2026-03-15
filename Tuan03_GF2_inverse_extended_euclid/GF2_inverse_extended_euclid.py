def degree(p):
    """Tra ve bac cua da thuc."""
    if p == 0:
        return -1
    return p.bit_length() - 1


def poly_div(a, b):
    """Chia da thuc tren GF(2): a = q*b + r"""
    q = 0
    r = a
    deg_b = degree(b)

    while r != 0 and degree(r) >= deg_b:
        shift = degree(r) - deg_b
        q ^= (1 << shift)
        r ^= (b << shift)

    return q, r


def poly_mul(a, b):
    """Nhan da thuc tren GF(2)."""
    p = 0
    while b:
        if b & 1:
            p ^= a
        a <<= 1
        b >>= 1
    return p


def poly_mod(a, m):
    """Lay modulo da thuc."""
    _, r = poly_div(a, m)
    return r


def poly_mul_mod(a, b, m):
    """Nhan da thuc roi mod m(x)."""
    return poly_mod(poly_mul(a, b), m)


def extended_euclid_gf2(a, m):
    """Thuat toan Euclidean mo rong tren GF(2)."""
    print(f"\nTim nghich dao cua: {a}")
    print(f"a (bin) = {bin(a)[2:]}")
    print(f"m(x)    = {bin(m)[2:]}")
    print("-" * 60)

    r0, r1 = m, a
    t0, t1 = 0, 1

    print(f"{'step':<5}{'q':>12}{'r':>18}{'t':>18}")
    print("-" * 60)
    
    print(f"{'-':<5}{'-':>12}{bin(r0)[2:]:>18}{bin(t0)[2:]:>18}")
    print(f"{'-':<5}{'-':>12}{bin(r1)[2:]:>18}{bin(t1)[2:]:>18}")

    step = 1

    while r1 != 0:
        q, r2 = poly_div(r0, r1)
        t2 = t0 ^ poly_mul(q, t1)

        print(f"{step:<5}{bin(q)[2:]:>12}{bin(r2)[2:]:>18}{bin(t2)[2:]:>18}")

        r0, r1 = r1, r2
        t0, t1 = t1, t2

        step += 1

    print("-" * 60)

    if r0 != 1:
        print("Khong ton tai nghich dao")
        return None

    print(f"Nghich dao = {t0}")
    print(f"Dang nhi phan = {bin(t0)[2:]}")

    return t0


if __name__ == "__main__":

    m = 1033   

    a = 523
    b = 1015

    inv_a = extended_euclid_gf2(a, m)
    inv_b = extended_euclid_gf2(b, m)

    print("\n" + "="*20)
    print("   KIEM TRA KET QUA   ")
    print("="*20)

    if inv_a is not None:
        check_a = poly_mul_mod(a, inv_a, m)
        print(f"{a} * {inv_a} mod m(x) = {check_a}")

    if inv_b is not None:
        check_b = poly_mul_mod(b, inv_b, m)
        print(f"{b} * {inv_b} mod m(x) = {check_b}")

    print("\n--- KET QUA CUOI ---")
    print(f"a^-1 ({a}^-1) = {inv_a}")
    print(f"b^-1 ({b}^-1) = {inv_b}")