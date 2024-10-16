import qrcode
#Whatsapp Qr code generator
# Your WhatsApp link (replace with your actual number)
whatsapp_link = "https://wa.me/03361157646"  # Replace with your phone number (with country code)

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(whatsapp_link)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the QR code as an image
img.save("whatsapp_qr_code.png")

print("QR code generated and saved as whatsapp_qr_code.png")
