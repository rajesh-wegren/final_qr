from django.db import models

# Create your models here.
class Qrcode(models.Model):
    user_url = models.URLField(max_length=200)


    def __str__(self):
        return self.user_url
        
    # def clean_user_url(self):
    # 	input_userurl = self.cleaned_data['user_url']
    # 	print('validation of urls id field')
    # 	return input_userurl