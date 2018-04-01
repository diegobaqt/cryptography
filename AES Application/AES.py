# By diegobaqt
# See more algorithms at https://github.com/diegobaqt/cryptography
# About pyaes: https://github.com/ricmoo/pyaes

from PIL import Image
import sys
import pyaes.aes
import base64
import io


def select_key(key_bits):
    key = ""
    if key_bits == 128:
        print "Enter your key (16 bytes)"
        key = sys.stdin.readline().strip()
        if len(key) > 16:
            print "Invalid value"
    elif key_bits == 192:
        print "Enter your key (24 bytes)"
        key = sys.stdin.readline().strip()
        if len(key) > 24:
            print "Invalid value"
    elif key_bits == 256:
        print "Enter your key (32 bytes)"
        key = sys.stdin.readline().strip()
        if len(key) > 32:
            print "Invalid value"
    else:
        print "Invalid value"
        get_encryption()

    return bytes(key)


# Encrypt the image
def get_encryption():
    print "Enter Image name (same folder):"
    image = sys.stdin.readline().strip()

    with open(image, "rb") as imageFile:
        image_bits = imageFile.read()

    print "Enter long of the key (128, 192 o 256 bits):"
    key_bits = int(sys.stdin.readline().strip())
    key = select_key(key_bits)

    aes = pyaes.AESModeOfOperationCTR(key)
    d = aes.encrypt(image_bits)

    print "Encrypted Message: %r" % d
    print "Encrypted Message with 64-bits encode: ", base64.b64encode(d)


# Decrypts the image
def get_decryption():
    print "Enter Encrypted Message"
    cipher_text = sys.stdin.readline().strip()
    d = base64.b64decode(cipher_text)

    print "Enter your key: "
    key = sys.stdin.readline().strip()

    aes = pyaes.AESModeOfOperationCTR(key)
    stream = io.BytesIO(aes.decrypt(d))
    img = Image.open(stream)
    img.save("mario_decifrado_aes.jpg")


if __name__ == "__main__":
    print "Enter the mode (Encrypt: 1. Decipher: 0)"
    mode = int(sys.stdin.readline().strip())
    if mode == 1:
        get_encryption()
    elif mode == 0:
        get_decryption()
    else:
        "Error: The mode is not valid (1: Encrypt, 0: Decipher)"
