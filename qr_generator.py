import qrcode
from datetime import datetime

def create_qr(data, filename):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    with open("history.txt", "a") as f:
        f.write(f"{datetime.now()} - {data} -> {filename}\n")

    print("✅ QR generated and logged")

if __name__ == "__main__":
    url = input("Enter the URL: ")
    filename = input("Output filename: ")
    create_qr(url, filename)
