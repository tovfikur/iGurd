from django.db import models

# Create your models here.


class AboutUsList(models.Model):
    Quot = models.CharField(max_length=60, null=True, blank=True)


class Index(models.Model):
    Header          = models.CharField(max_length=60, blank=False, null=False, default= 'The Safest Way to Pay')
    HeaderQuot      = models.TextField(max_length=150, blank=False, null=False, default= 'Lorem Ipsum is text industry. Ipsum has been the industry\'s standard dummy text. Lorem Ipsum is simply dummy text of the printing.')
    AboutUsTitle    = models.CharField(max_length=60, blank=False, null=False, default= 'Lorem Ipsum is text industry. Ipsum has been the industry\'s standard dummy text. Lorem Ipsum is simply dummy text of the printing.')
    AboutUsQuot     = models.TextField(max_length=200, blank=False, null=False, default= 'Lorem ipsum dolor sit amet.')
    AboutUsList     = models.ManyToManyField(AboutUsList, blank=True)
    BuyerQuot       = models.TextField(max_length=200, blank=False, null=False, default= 'Lorem Ipsum is text industry. Ipsum has been the industry\'s standard dummy text. Lorem Ipsum is simply dummy text of the printing.')
    SellerQuot      = models.TextField(max_length=200, blank=False, null=False, default= 'Lorem Ipsum is text industry. Ipsum has been the industry\'s standard dummy text. Lorem Ipsum is simply dummy text of the printing.')
    SecureTitle     = models.CharField(max_length=100, blank=False, null=False, default= 'SAFE & SECURE & NO ADVANCE PAYMENT RISK')
    SecureQuot      = models.TextField(max_length=200, blank=False, null=False, default= 'Lorem Ipsum is text industry. Ipsum has been the industry\'s standard dummy text. Lorem Ipsum is simply dummy text of the printing.')
    TrusTitle       = models.CharField(max_length=100, blank=False, null=False, default= 'Lorem Ipsum is text industry. Ipsum has been the industry\'s standard dummy text. Lorem Ipsum is simply dummy text of the printing.')
    TrustQuot       = models.TextField(max_length=200, blank=False, null=False, default= 'Lorem Ipsum is text industry. Ipsum has been the industry\'s standard dummy text. Lorem Ipsum is simply dummy text of the printing.')
    SupportTitle    = models.CharField(max_length=100, blank=False, null=False, default= 'Lorem Ipsum is text industry. Ipsum has been the industry\'s standard dummy text. Lorem Ipsum is simply dummy text of the printing.')
    SupportQuot     = models.TextField(max_length=200, blank=False, null=False, default= 'Lorem Ipsum is text industry. Ipsum has been the industry\'s standard dummy text. Lorem Ipsum is simply dummy text of the printing.')
    TestimonialsQuot= models.TextField(max_length=200, blank=False, null=False, default= 'Lorem Ipsum is text industry. Ipsum has been the industry\'s standard dummy text. Lorem Ipsum is simply dummy text of the printing.')
    FooterQuot      = models.TextField(max_length=300, blank=False, null=False, default= 'Lorem Ipsum is text industry. Ipsum has been the industry\'s standard dummy text. Lorem Ipsum is simply dummy text of the printing.')


class Testimonials(models.Model):
    Name = models.CharField(max_length=30, blank=False, null=False, default="Tovfikur Rahman")
    Rank = models.CharField(max_length=20, blank=False, null=False, default='Developer')
    Quot = models.CharField(max_length=100, blank=False, null=False, default='Lunch is not free')


class PartnerList(models.Model):
    Name = models.CharField(max_length=30, blank=False, null=False, default='RayBim Tech.')
    Logo = models.ImageField(blank=True, null=True)


class PaymentPartner(models.Model):
    Name = models.CharField(max_length=30, blank=False, null=False, default='RayBim Tech.')
    Logo = models.ImageField(blank=True, null=True)
