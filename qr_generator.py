import qrcode

def create_qr(data, filename="my_qr.png"):
    if not data.strip():
        print("❌ URL cannot be empty")
        return

    if not filename.endswith(".png"):
        filename += ".png"

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    print("✅ QR code generated successfully!")
    print(f"📁 Saved as: {filename}")

if __name__ == "__main__":
    url = input("Enter the URL: ")
    filename = input("Enter output file name: ")
    create_qr(url, filename)
