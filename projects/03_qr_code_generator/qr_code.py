import qrcode
import cv2
import os  

def generate_qr(data, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"✅ QR Code saved as {filename}")

    try:
        os.system(f'start {filename}')  
    except Exception as e:
        print(f"❌ Unable to open image: {e}")

def decode_qr(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)

    if bbox is not None:
        print(f"✅ QR Code Data: {data}")
    else:
        print("❌ No QR code found in the image.")

if __name__ == "__main__":
    option = input("Enter '1' to generate QR code, '2' to decode QR code: ")

    if option == "1":
        text = input("Enter text to encode in QR code: ")
        filename = input("Enter filename (default: qrcode.png): ") or "qrcode.png"
        generate_qr(text, filename)
    elif option == "2":
        filename = input("Enter QR code image filename: ")
        decode_qr(filename)
    else:
        print("❌ Invalid option selected!")
