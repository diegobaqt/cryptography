# By diegobaqt
# See more algorithms at https://github.com/diegobaqt/cryptography
import sys


def get_encryption(p, k):
    cipher_array = []
    for ch in range(len(p)):
        cipher_array.append((p[ch]+k[ch]) % 26)
    return ''.join(chr(i + 65) for i in cipher_array)


def get_decryption(c, k):
    plaintext_array = []
    for ch in range(len(c)):
        plaintext_array.append((c[ch]-k[ch]) % 26)
    return ''.join(chr(i + 65) for i in plaintext_array)


def change_input(t1, t2):
    p = []
    k = []
    for ch in range(len(t1)):
        p.append(ord(t1[ch]) - 65)
        k.append(ord(t2[ch]) - 65)
    return p, k

# To receive message in plaintext #
plaintext = sys.stdin.readline().upper().strip()

# To receive key #
key = sys.stdin.readline().upper().strip()

plaintext_numerical, key_numerical = change_input(plaintext, key)

# Encryption
cipher_text = get_encryption(plaintext_numerical, key_numerical)
print "Encrypted Message:", cipher_text

# To receive cipher text #
cipher_text = sys.stdin.readline().upper().strip()

# To receive key #
key = sys.stdin.readline().upper().strip()

# Decryption
cipher_text_numerical, key_numerical = change_input(cipher_text, key)
plaintext_decrypted = get_decryption(cipher_text_numerical, key_numerical)
print "Decrypted Message:", plaintext_decrypted



