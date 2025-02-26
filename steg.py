import cv2
import os
import string

file_path = input("Enter the file location of the image: ")
img = cv2.imread(file_path)

if img is None:
    print("Error: Unable to open image file.")
    exit()

msg = input("Enter secret message: ")
password = input("Enter password: ")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

output_path = "Encryptedmsg.jpg"
cv2.imwrite(output_path, img)

os.system(f"start {output_path}")

message = ""

n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption")

if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n,m,z]]
        n=n+1
        m=m+1
        z=(z+1) % 3
    print("Decryption message",message)
else:
    print("Not valid key")
