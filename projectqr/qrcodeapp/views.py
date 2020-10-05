from django.shortcuts import render
from qrcodeapp.models import Qrcode
from qrcodeapp.forms import QrForm
import qrcode


# Create your views here.
def home_page(request):
    return render(request=request, template_name='qrcodeapp/homepage.html')


def thank_you(request):
    return render(request=request, template_name='qrcodeapp/thankyou.html')


def qr_data(request):
    qr_form = QrForm()
    if request.method == 'GET':

        if request.method == 'POST':
            form_data = QrForm(request.POST)
            if form_data.is_valid():
                form_data.save(commit=True)

    if request.method == "POST":
        form_data = QrForm(request.POST)
        if form_data.is_valid():
            # print(f'user_url:{form_data.cleaned_data["user_url"]}')
            print('user_url:', form_data.cleaned_data['user_url'])

            # new upadte
            # Create qr code instance
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )

            # The data that you want to store
            # data = "The Data that you need to store in the QR Code"
            # data = input("Enete the data : ")

            # Add data
            qr.add_data(form_data)
            qr.make(fit=True)

            # Create an image from the QR Code instance
            img = qr.make_image()

            # Save it somewhere, change the extension as needed:
            # img.save("image.png")
            # img.save("image.bmp")
            # img.save("image.jpeg")
            img.save("image.jpg")

            form_data.save(commit=True)
            return thank_you(request)

    my_dict = {'qr_form': qr_form}

    return render(request=request, template_name='qrcodeapp/qrcreate.html', context=my_dict)

