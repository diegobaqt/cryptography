# By diegobaqt
# See more algorithms at https://github.com/diegobaqt/cryptography
import sys
import numpy


def get_encryption(m, k):
    while len(m) < size:
        m += 'A'
    m1 = m
    matrix = [x[:] for x in [[''] * size] * size]
    while len(m1) > 0:
        for i in xrange(size):
            for j in xrange(size):
                if k[i][j] == 1 and matrix[i][j] == '':
                    matrix[i][j] = m1[0]
                    m1 = m1[1:]
        if rotation == 1:
            k = numpy.rot90(k)
        elif rotation == 0:
            k = numpy.rot90(numpy.rot90(numpy.rot90(k)))
        else:
            return "Error: The rotation is not valid (Clockwise: 1. Anticlockwise: 0)"
    array_cipher = [y for x in matrix for y in x]
    return ''.join(map(str, array_cipher))


def get_decryption(c, k):
    matrix = [x[:] for x in [[''] * size] * size]
    visited_matrix = numpy.zeros((size, size))
    index_cipher = 0
    plain_text = ""
    for i in xrange(size):
        for j in xrange(size):
            matrix[i][j] = c[index_cipher]
            index_cipher += 1

    index_cipher = 0
    while index_cipher < len(c):
        for i in xrange(size):
            for j in xrange(size):
                if k[i][j] == 1 and visited_matrix[i][j] == 0:
                    plain_text += matrix[i][j]
                    visited_matrix[i][j] = 1
                    index_cipher += 1
        if rotation == 1:
            k = numpy.rot90(k)
        elif rotation == 0:
            k = numpy.rot90(numpy.rot90(numpy.rot90(k)))
        else:
            return "Error: The rotation is not valid (Clockwise: 1. Anticlockwise: 0)"
    return plain_text


if __name__ == "__main__":
    # To receive grille size #
    print "Enter the size of the matrix"
    size = int(sys.stdin.readline())

    # To receive direction #
    print "Enter the rotation (Clockwise: 1. Anticlockwise: 0)"
    rotation = int(sys.stdin.readline())

    # To receive mode #
    print "Enter the mode (Encrypt: 1. Decipher: 0)"
    mode = int(sys.stdin.readline())

    # To receive holes #
    print "Enter the location of the holes separated by spaces (Example: '2,4 4,4, 1,3' )"
    holes = sys.stdin.readline().strip().split(" ")

    grille = numpy.zeros((size, size))
    for n in xrange(len(holes)):
        x, y = map(int, holes[n].split(","))
        grille[x-1][y-1] = 1

    if mode == 1:
        # Encryption
        print "Enter the message you want to encrypt"
        message = sys.stdin.readline().strip()
        if len(message) > size*size:
            print "The size of the message can not exceed the number of cells in the grid"
        else:
            print "Encrypted Message: ", get_encryption(message, grille)
    elif mode == 0:
        # Decryption
        print "Enter the message you want to decrypt"
        cipher_text = sys.stdin.readline().strip()
        print "Decrypted Message:", get_decryption(cipher_text, grille)
    else:
        print "Error: The mode is not valid (1: Encrypt, 0: Decipher)"



