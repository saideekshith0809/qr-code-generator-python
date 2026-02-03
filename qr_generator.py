import qrcode

def create_qr(data, filename, fill_color, back_color):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color=fill_color,
        back_color=back_color
    )
    img.save(filename)

    print("✅ QR code generated")
    print(f"🎨 Colors: {fill_color} on {back_color}")
    print(f"📁 Saved as: {filename}")

if __name__ == "__main__":
    url = input("Enter the URL: ")
    filename = input("Output filename (with .png): ")
    fill = input("QR color (black/blue/red): ")
    back = input("Background color (white/yellow): ")

    create_qr(url, filename, fill, back)
