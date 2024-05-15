from PIL import Image

def encrypt_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    encrypted_pixels = []

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            # Example of a simple operation: add 50 to each pixel value
            r = (r + 50) % 256
            g = (g + 50) % 256
            b = (b + 50) % 256
            encrypted_pixels.append((r, g, b))

    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully.")


def decrypt_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    decrypted_pixels = []

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            # Reverse the encryption operation: subtract 50 from each pixel value
            r = (r - 50) % 256
            g = (g - 50) % 256
            b = (b - 50) % 256
            decrypted_pixels.append((r, g, b))

    decrypted_img = Image.new(img.mode, img.size)
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully.")


def main():
    image_path = input("Enter the path to the image file: ")
    encrypt_or_decrypt = input("Encrypt or Decrypt? (E/D): ")

    if encrypt_or_decrypt.lower() == 'e':
        encrypt_image(image_path)
    elif encrypt_or_decrypt.lower() == 'd':
        decrypt_image(image_path)
    else:
        print("Invalid choice. Please enter 'E' for encrypt or 'D' for decrypt.")


if __name__ == "__main__":
    main()
