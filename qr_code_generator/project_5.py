# # runthis commannd in your terminal first pip install qrcode[pil]
# This allows Python to generate QR codes.
import qrcode
# This line imports the qrcode module, which provides tools for generating QR codes.


# Data to be stored in the QR code
data = "QR code using QRCode class"
# This is the text or data that you want to store in the QR code.
# When someone scans the QR code, they will see this text.

# Create a QRCode object
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
# Here, we create a QRCode object with three important settings:

# version=1:
# Controls the size of the QR code.
# Version 1 is the smallest, and higher numbers make bigger QR codes.
# box_size=10:
# Each small square (pixel) inside the QR code will be 10x10 pixels in size.
# border=5:
# This adds a 5-box-wide white border around the QR code.


# Add data to the QR code
qr.add_data(data)
# This adds the text (data) to the QR code object.
qr.make(fit=True)
# This converts the added data into a QR code.
# The fit=True argument makes sure the QR code adjusts automatically to fit the data properly.

# Create an image from the QR Code instance
img = qr.make_image(fill="black", back_color="white")
# This creates a QR code image with:
# fill="black" → QR code squares will be black.
# back_color="white" → Background will be white.

# Save the image
img.save("qr_code_project_7.png")
# This saves the QR code as an image file named "qr_code_project_7.png" in the same folder as your script.
# You can open this image and scan it using a QR code scanner or a phone camera.🚀🐍
