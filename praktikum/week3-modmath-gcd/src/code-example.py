# ==============================================
# Program: Kriptografi Dasar dengan Python (CLI)
# Fitur:
# 1. Operasi aritmetika modular
# 2. Menentukan bilangan prima dan GCD
# 3. Logaritma diskrit & simulasi kriptografi
# ==============================================

from math import isqrt
import random

# ======== Bagian Fungsi Dasar ========

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        g, x1, y1 = egcd(b, a % b)
        return (g, y1, x1 - (a // b) * y1)

def mod_inv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError(f"Tidak ada invers modular untuk {a} mod {m}")
    return x % m

def is_prime(n):
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    bases = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    for a in bases:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True

# ======== Logaritma Diskrit (BSGS) ========

def discrete_log_bsgs(g, h, p):
    n = isqrt(p) + 1
    baby = {}
    cur = 1
    for j in range(n):
        baby[cur] = j
        cur = (cur * g) % p
    g_n_inv = pow(pow(g, n, p), -1, p)
    gamma = h
    for i in range(n+1):
        if gamma in baby:
            return i * n + baby[gamma]
        gamma = (gamma * g_n_inv) % p
    return None

# ======== Diffie-Hellman Sederhana ========

def diffie_hellman_sim(p, g):
    a = random.randint(2, p - 2)
    b = random.randint(2, p - 2)
    A = pow(g, a, p)
    B = pow(g, b, p)
    s1 = pow(B, a, p)
    s2 = pow(A, b, p)
    return {
        "p": p, "g": g,
        "a": a, "b": b,
        "A": A, "B": B,
        "shared": s1
    }

# ======== Menu CLI ========

def menu():
    while True:
        print("\n=== MENU KRIPTOGRAFI DASAR ===")
        print("1. Operasi Aritmetika Modular")
        print("2. Cek Bilangan Prima & Hitung GCD")
        print("3. Logaritma Diskrit & Simulasi Kriptografi")
        print("4. Keluar")

        pilih = input("Pilih menu (1-4): ")

        if pilih == "1":
            a = int(input("Masukkan a: "))
            b = int(input("Masukkan b: "))
            m = int(input("Modulus m: "))
            print(f"{a} + {b} mod {m} = {(a+b)%m}")
            print(f"{a} - {b} mod {m} = {(a-b)%m}")
            print(f"{a} × {b} mod {m} = {(a*b)%m}")
            print(f"{a}^{b} mod {m} = {pow(a,b,m)}")
            try:
                inv = mod_inv(a, m)
                print(f"Invers modular {a} mod {m} = {inv}")
            except Exception as e:
                print(e)

        elif pilih == "2":
            n = int(input("Masukkan bilangan untuk diuji prima: "))
            print(f"{n} {'adalah' if is_prime(n) else 'bukan'} bilangan prima.")
            a = int(input("Masukkan bilangan pertama (untuk GCD): "))
            b = int(input("Masukkan bilangan kedua (untuk GCD): "))
            print(f"GCD({a}, {b}) = {gcd(a,b)}")

        elif pilih == "3":
            print("\n=== Logaritma Diskrit & Diffie-Hellman ===")
            p = int(input("Masukkan bilangan prima p: "))
            g = int(input("Masukkan generator g: "))
            secret = random.randint(2, p - 2)
            h = pow(g, secret, p)
            print(f"Nilai publik h = g^x mod p = {h} (x disembunyikan)")
            x = discrete_log_bsgs(g, h, p)
            print(f"Logaritma diskrit ditemukan: x = {x}")
            print("\nSimulasi Diffie-Hellman:")
            dh = diffie_hellman_sim(p, g)
            print(f"A = g^a mod p = {dh['A']}")
            print(f"B = g^b mod p = {dh['B']}")
            print(f"Shared secret = {dh['shared']}")

        elif pilih == "4":
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

# ======== Jalankan ========
if _name_ == "_main_":
    menu()
