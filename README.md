# Edunet-Final-Project

Image-Based Steganography and Encryption Tool

This Python program provides a basic method for hiding secret messages within an image. It encrypts a text message by altering the pixel values of the image and requires a passcode to decrypt and reveal the hidden message.

## Features:
- **Encryption**: Hides a secret message inside an image file using pixel manipulation.
- **Decryption**: Reveals the hidden message from the image using the correct passcode.
- **User-friendly Interface**: Simple prompts to input the file location, secret message, and passcode.

## Technologies Used:
- **Python**: The program is written in Python, a powerful programming language.
- **OpenCV (cv2)**: The OpenCV library is used to read, modify, and save the image file.
- **OS Module**: Utilized to open the encrypted image in the default image viewer.
- **Dictionaries**: The program uses dictionaries to map characters to pixel values and vice versa.
- **Basic Image Steganography**: The encryption is done by manipulating pixel values to encode the message.

## Installation Instructions:
1. **Install Python 3.x**: Ensure you have Python 3.x installed on your system. You can download it from the official Python website: [Python Downloads](https://www.python.org/downloads/)
2. **Install Dependencies**: This program requires the OpenCV library. You can install it using pip:
    ```bash
    pip install opencv-python
    ```
3. **Clone/Download the Repository**: If you're using a repository, clone it to your local machine using:
    ```bash
    git clone <repository_url>
    ```
    Or simply download the Python file.

## Usage Instructions:
1. **Run the Program**:
    Navigate to the directory where the Python file is located and execute it with Python:
    ```bash
    python steganography_encrypt.py
    ```
2. **Input Details**:
    - **Image File Location**: The program will prompt you to enter the file path of the image you want to encrypt.
    - **Secret Message**: You will be asked to input the message you wish to hide inside the image.
    - **Password**: Enter a passcode that will be required for decryption.
3. **Encryption**:
    - The image will be modified to hide the secret message, and the encrypted image will be saved as `Encryptedmsg.jpg` in the same directory.
    - The program will automatically open the encrypted image using your default image viewer.
4. **Decryption**:
    - To decrypt the message, run the program again, provide the encrypted image, and enter the correct passcode when prompted.
    - If the correct password is entered, the hidden message will be revealed.

## Example:
### Encrypting a message:
```arduino
Enter the file location of the image: image.jpg
Enter secret message: Hello, this is a secret message!
Enter password: mysecurepassword
