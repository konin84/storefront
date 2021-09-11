from django.contrib import admin
from .models import *
admin.site.site_header = "Store Front Management System admin"
admin.site.site_title = "Store Front Management System admin area"
admin.site.index_title = "Welcome to the Store Front Management System admin area"

@admin.register(About_us,CompanyInfo, ContactUs, Product, Slide, Staff)
class ViewAdmin(admin.ModelAdmin):
    pass