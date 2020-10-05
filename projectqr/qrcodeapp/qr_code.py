#
# Import QR Code library
import qrcode

# Create qr code instance
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)

# The data that you want to store
# data = "The Data that you need to store in the QR Code"
data=input("Enete the data : ")

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image()

# Save it somewhere, change the extension as needed:
# img.save("image.png")
# img.save("image.bmp")
# img.save("image.jpeg")
img.save("image.jpg")

#
# #
# # #  2nd MENTHOD OF QR CODE GENERATE ___
# # import pyqrcode
# # def generate_qr():
# #     link_to_post = "https://medium.com/@ngengesenior/qr-codes-generation-with-python-377735be6c5f"
# #     url = pyqrcode.create(link_to_post)
# #     url.svg('url.jpg', scale=8)
# #     print("Printing QR code")
# #     print(url.terminal())
# #
# #
# # if __name__ == '__main__':
# #     generate_qr()