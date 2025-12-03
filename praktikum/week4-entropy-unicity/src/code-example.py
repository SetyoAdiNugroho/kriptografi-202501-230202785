#!/usr/bin/env python3
# caesar_crypto_metrics.py
# CLI sederhana: analisis entropi, unicity distance, dan brute-force khusus Caesar cipher

import math
from typing import Iterable, Tuple

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET_SIZE = len(ALPHABET)  # 26

# ---------------- Core crypto-metrics ----------------

def entropy_bits_from_keyspace(keyspace_size: int) -> float:
    if keyspace_size <= 0:
        raise ValueError("keyspace_size harus > 0")
    return math.log2(keyspace_size)

def estimate_redundancy_bits_per_char(alphabet_size: int = ALPHABET_SIZE,
                                      empirical_entropy_per_char_bits: float = None) -> float:
    max_bits = math.log2(alphabet_size)
    empirical = empirical_entropy_per_char_bits if empirical_entropy_per_char_bits is not None else 1.5
    R = max_bits - empirical
    return max(R, 0.0)

def unicity_distance_bits(key_entropy_bits: float, redundancy_bits_per_char: float) -> float:
    if redundancy_bits_per_char <= 0:
        raise ValueError("redundancy_bits_per_char harus > 0")
    return key_entropy_bits / redundancy_bits_per_char

def seconds_to_readable(seconds: float) -> str:
    if seconds <= 0:
        return "0 detik"
    units = [
        ("tahun", 365*24*3600),
        ("hari", 24*3600),
        ("jam", 3600),
        ("menit", 60),
        ("detik", 1)
    ]
    parts = []
    rem = int(seconds)
    for name, sec_unit in units:
        if rem >= sec_unit:
            qty = rem // sec_unit
            rem %= sec_unit
            parts.append(f"{qty} {name}")
    return ", ".join(parts) if parts else "0 detik"

def estimate_bruteforce_time(keyspace_size: int, attempts_per_second: float,
                             mode: str = "average") -> Tuple[float,str]:
    if keyspace_size <= 0:
        raise ValueError("keyspace_size harus > 0")
    if attempts_per_second <= 0:
        raise ValueError("attempts_per_second harus > 0")
    mode = mode.lower()
    if mode == "best":
        attempts = 1
    elif mode == "average":
        attempts = keyspace_size / 2.0
    elif mode == "worst":
        attempts = keyspace_size
    else:
        raise ValueError("mode harus salah satu dari: best, average, worst")
    seconds = attempts / attempts_per_second
    return seconds, seconds_to_readable(seconds)

# ---------------- Caesar cipher helpers ----------------

def caesar_encrypt(plaintext: str, key: int) -> str:
    key = key % ALPHABET_SIZE
    out = []
    for ch in plaintext:
        if ch.isalpha():
            is_upper = ch.isupper()
            base = 'A' if is_upper else 'a'
            shifted = chr((ord(ch) - ord(base) + key) % ALPHABET_SIZE + ord(base))
            out.append(shifted)
        else:
            out.append(ch)
    return "".join(out)

def caesar_decrypt(ciphertext: str, key: int) -> str:
    return caesar_encrypt(ciphertext, -key)

def caesar_bruteforce(ciphertext: str):
    """Mengembalikan list (key, candidate_plaintext) untuk semua kunci 0..25"""
    results = []
    for k in range(ALPHABET_SIZE):
        pt = caesar_decrypt(ciphertext, k)
        results.append((k, pt))
    return results

# ---------------- CLI ----------------

def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except Exception:
            print("Masukkan angka valid (contoh 1e6 atau 1000). Coba lagi.")

def menu():
    print("=== Caesar Cipher Metrics ===")
    while True:
        print("\nMenu:")
        print("1) Info dasar Caesar (keyspace & entropi)")
        print("2) Hitung unicity distance (asumsi bahasa)")
        print("3) Estimasi brute-force attack untuk Caesar")
        print("4) Demonstrasi brute-force (tampilkan semua kandidat dekripsi)")
        print("5) Keluar")
        pilihan = input("Pilih (1-5): ").strip()
        if pilihan == "1":
            ks = ALPHABET_SIZE
            H = entropy_bits_from_keyspace(ks)
            print(f"Keyspace Caesar: {ks} kemungkinan (kunci 0..{ks-1})")
            print(f"Entropi kunci ≈ {H:.3f} bits")
        elif pilihan == "2":
            H = entropy_bits_from_keyspace(ALPHABET_SIZE)
            emp = input("Estimasi entropi per karakter (bits) [enter=1.5 untuk bahasa Inggris]: ").strip()
            emp_val = float(emp) if emp else 1.5
            R = estimate_redundancy_bits_per_char(ALPHABET_SIZE, emp_val)
            U = unicity_distance_bits(H, R)
            print(f"Redundansi ≈ {R:.3f} bits/char -> Unicity distance ≈ {U:.3f} karakter")
            print("Artinya: sekitar jumlah karakter ciphertext sepanjang nilai ini diperlukan agar kunci unik.")
        elif pilihan == "3":
            rate = read_float("Masukkan attempts per second (mis. 1000): ")
            for mode in ("best","average","worst"):
                sec, pretty = estimate_bruteforce_time(ALPHABET_SIZE, rate, mode)
                print(f"{mode.capitalize():7s}: {pretty} (≈ {sec:.3f} detik)")
        elif pilihan == "4":
            ct = input("Masukkan ciphertext: ")
            results = caesar_bruteforce(ct)
            print("\nHasil brute-force (key -> plaintext):")
            for k, pt in results:
                print(f"{k:2d}: {pt}")
            print("\nPilih kandidat yang terlihat benar.")
        elif pilihan == "5":
            print("Keluar.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    menu()
