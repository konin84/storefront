from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from froala_editor.fields import FroalaField
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib import messages
from .helpers import *

class ContactUs(models.Model):
    name = models.CharField ( max_length=50)
    subject = models.CharField(max_length=50, null=True, blank=True)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=50)
    message = FroalaField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Contact_us'

class CompanyInfo(models.Model):
    name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=50)
    located_at = FroalaField()
    description = FroalaField()
    image = models.ImageField(null=True, upload_to='company/photo')
    tweeter = models.CharField(max_length=300, null=True, blank=True)
    facebook = models.CharField(max_length=300, null=True, blank=True)
    youtube = models.CharField(max_length=300, null=True, blank=True)
    instagram = models.CharField(max_length=300, null=True, blank=True)

    def clean(self):
        if CompanyInfo.objects.exists() and not self.pk:
            raise ValidationError("Company information already recorded")
    def save(self, *args, **kwargs):
        return super(CompanyInfo, self).save(*args, **kwargs)
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'CompanyInfo'


class Product(models.Model):
    registered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    intro = models.CharField(max_length=100, null=True, blank=True)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='product/product_images')
    date_posted = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('main:product_detail', kwargs={'slug': self.slug})
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Product, self).save(*args, **kwargs)


class About_us(models.Model):
    about_company = FroalaField()
    vision_and_values = FroalaField()
    lead_structure = FroalaField()
    our_belief = FroalaField()
    customer_support = FroalaField()
    sustainability =FroalaField()
    our_quality = FroalaField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def clean(self):
        if About_us.objects.exists() and not self.pk:
            raise ValidationError("About us already exists")
    def save(self, *args, **kwargs):
        return super(About_us, self).save(*args, **kwargs)
    def __str__(self):
        return f' About us posted on: {self.date_posted}'
    class Meta:
        verbose_name_plural = 'About_us'


class Slide(models.Model):
    slideBtnText = models.CharField(max_length=20)
    slide1name= models.CharField(max_length=100)
    slide1text = FroalaField()
    slide2name = models.CharField(max_length=100 )
    slide2text = FroalaField ()
    slide3name = models.CharField(max_length=100)
    slide3text = FroalaField ()
    def clean(self):
        if Slide.objects.exists() and not self.pk:
            raise ValidationError("Slide info already exists")
    def save(self, *args, **kwargs):
        return super(Slide, self).save(*args, **kwargs)
    def __str__(self):
        return self.slideBtnText



class Staff(models.Model):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    CIVILITY = \
        [('Mrs.', 'Mrs.'), ('Mr.', 'Mr.'), ('Other', 'Other'), ]

    ROLE = \
        [('Administrator', 'Administrator' ),
         ('Webmaster',  'Webmaster' ),]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=10, choices=GENDER, default='Male')
    civility = models.CharField(max_length=15, choices=CIVILITY, default='Mrs.')
    position_to_hold = models.CharField(max_length=15, choices=ROLE, default='Webmaster')
    email = models.EmailField(max_length=50)
    telephone_number = PhoneNumberField()
    description = FroalaField(null=True, blank=True, default='I work with company')
    Date_joined = models.DateField ( null=True, blank=True )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def fullname(self):
        return f'{self.first_name} {self.last_name}'

