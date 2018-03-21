# By diegobaqt
# See more algorithms at https://github.com/diegobaqt/cryptography

from PIL import Image
import sys
import pyDes
import base64
import io
import IPython


# Encrypt the image
def get_encryption():
    print "Enter Image name (same folder):"
    image = sys.stdin.readline().strip()

    with open(image, "rb") as imageFile:
        image_bits = imageFile.read()

    print "Enter your key (8-bytes): "
    key = sys.stdin.readline().strip()

    k = pyDes.des(key, pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    d = k.encrypt(image_bits)
    print "Encrypted Message: %r" % d
    print "Encrypted Message with 64-bits encode: ", base64.b64encode(d)


# Decrypts the image
def get_decryption():
    print "Enter Encrypted Message"
    cipher_text = sys.stdin.readline().strip()
    d = base64.b64decode(cipher_text)

    print "Enter your key (8-bytes): "
    key = sys.stdin.readline().strip()

    k = pyDes.des(key, pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)

    stream = io.BytesIO(k.decrypt(d))
    img = Image.open(stream)
    img.save("mario_decifrado.jpg")
    IPython.display.Image("mario_decifrado.jpg")

if __name__ == "__main__":
    print "Enter the mode (Encrypt: 1. Decipher: 0)"
    mode = int(sys.stdin.readline().strip())
    if mode == 1:
        get_encryption()
    elif mode == 0:
        get_decryption()
    else:
        "Error: The mode is not valid (1: Encrypt, 0: Decipher)"




