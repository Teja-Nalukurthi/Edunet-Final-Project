# Edunet-Final-Project
Image-Based Steganography and Encryption Tool
This Python program provides a basic method for hiding secret messages within an image. It encrypts a text message by altering the pixel values of the image and requires a passcode to decrypt and reveal the hidden message.

Features:
Encryption: Hides a secret message inside an image file using pixel manipulation.
Decryption: Reveals the hidden message from the image using the correct passcode.
User-friendly Interface: Simple prompts to input the file location, secret message, and passcode.
Technologies Used:
Python: The program is written in Python, a powerful programming language.
OpenCV (cv2): The OpenCV library is used to read, modify, and save the image file.
OS Module: Utilized to open the encrypted image in the default image viewer.
Dictionaries: The program uses dictionaries to map characters to pixel values and vice versa.
Basic Image Steganography: The encryption is done by manipulating pixel values to encode the message.
Installation Instructions:
Install Python 3.x: Ensure you have Python 3.x installed on your system. You can download it from the official Python website: https://www.python.org/downloads/

Install Dependencies: This program requires the OpenCV library. You can install it using pip:

bash
Copy
pip install opencv-python
Clone/Download the Repository: If you're using a repository, clone it to your local machine using:

bash
Copy
git clone <repository_url>
Or simply download the Python file.

Usage Instructions:
Run the Program:

Navigate to the directory where the Python file is located and execute it with Python:
bash
Copy
python steganography_encrypt.py
Input Details:

Image File Location: The program will prompt you to enter the file path of the image you want to encrypt.
Secret Message: You will be asked to input the message you wish to hide inside the image.
Password: Enter a passcode that will be required for decryption.
Encryption:

The image will be modified to hide the secret message, and the encrypted image will be saved as Encryptedmsg.jpg in the same directory.
The program will automatically open the encrypted image using your default image viewer.
Decryption:

To decrypt the message, run the program again, provide the encrypted image, and enter the correct passcode when prompted.
If the correct password is entered, the hidden message will be revealed.
Example:
Encrypting a message:

arduino
Copy
Enter the file location of the image: image.jpg
Enter secret message: Hello, this is a secret message!
Enter password: mysecurepassword
Decrypting the message:

kotlin
Copy
Enter passcode for Decryption: mysecurepassword
Decryption message: Hello, this is a secret message!
System Requirements:
Operating System: Works on Windows, macOS, and Linux.
Python Version: Python 3.x.
Required Libraries: OpenCV library (opencv-python).
Hardware:
At least 2GB of RAM.
A modern processor (Intel Core i3 or higher recommended).
Adequate storage for image files.
Limitations:
Security: This encryption method is simple and intended for educational purposes. It is not suitable for highly sensitive information. Stronger encryption algorithms (e.g., AES) should be used for robust security.
Image Quality: The image may experience slight changes in pixel colors during encryption, but the changes are typically not noticeable to the human eye.
License:
This program is provided free of charge for personal and educational use. You are free to modify or distribute the code under the terms of the license, as long as proper attribution is given.
