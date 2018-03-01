# By diegobaqt
# Learn more about Hill Cipher in http://crypto.interactive-maths.com/hill-cipher.html
import sys
import numpy


def get_inverse_det(det):
    inv = 0
    for i in xrange(26):
        if (det * i) % 26 == 1:
            inv = i
    return inv


def get_inverse(k):
    # Calculate determinant
    det = (k[0][0]*k[1][1] - k[1][0]*k[0][1]) % 26

    # Get the multiplicative inverse of the determinant working modulo 26
    det_inv = get_inverse_det(det)

    # Calculate adjoin matrix of the key
    adj = numpy.array([[k[1][1], - k[0][1]], [-k[1][0], k[0][0]]])

    return (det_inv * adj) % 26


# Encrypt the message m with the key k
def get_encryption(k, m):
    cipher_array = ""
    if len(m) % 2 != 0:
        m += 'A'
    vectors = [m[x:x + 2] for x in xrange(0, len(m), 2)]

    for char in range(len(vectors)):
        vector = numpy.array([ord(vectors[char][0]) - 65, ord(vectors[char][1]) - 65])
        cipher_array += ''.join(chr((vector.dot(k)[0] % 26) + 65)) + ''.join(chr((vector.dot(k)[1] % 26) + 65))
    return cipher_array


# Decrypts the cipher text c with the key k
def get_decryption(c, k):
    inv_key = get_inverse(k)
    plaintext_array = []
    vectors = [c[x:x + 2] for x in xrange(0, len(c), 2)]
    for ch in range(len(vectors)):
        vector = numpy.array([ord(vectors[ch][0]) - 65, ord(vectors[ch][1]) - 65])
        plaintext_array.append(int(round(vector.dot(inv_key)[0])) % 26)
        plaintext_array.append(int(round(vector.dot(inv_key)[1])) % 26)
    return ''.join(chr(int(i) + 65) for i in plaintext_array)


# To receive message in plaintext #
message = sys.stdin.readline().strip()

# To receive key matrix #
a11, a12, a21, a22 = map(int, sys.stdin.readline().strip().split(" "))

# Build key matrix with numpy #
key = numpy.array([[a11, a12], [a21, a22]])

# Encrypt the message and print cipher text #
cipher_text = get_encryption(key, message)
print "El texto cifrado es: ", cipher_text

plaintext = get_decryption(cipher_text, key)
print "El mensaje es descifrado es: ", plaintext








