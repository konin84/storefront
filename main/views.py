from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from django.core.paginator import Paginator


def welcome(request):
    try:
        comp_info = CompanyInfo.objects.all()
        qs1 = Slide.objects.all()
        qs = About_us.objects.all()
        arg = {'title': 'welcome', 'page_name': 'welcome', 'data_set':qs, 'data_set1':qs1,'comp_info':comp_info,}
        return render(request, 'main/public/welcome.html', arg)
    except NameError:
        messages.error("Up... something went wrong...")


def about_us(request):
    comp_info = CompanyInfo.objects.all()
    qs1 = About_us.objects.all()
    qs2 = CompanyInfo.objects.all()
    arg = {'title': 'about us', 'page_name': 'about us', 'data_set1':qs1, 'data_set2': qs2, 'comp_info':comp_info,}
    return render ( request, 'main/public/about_us.html', arg )


def add_new_product(request):
    comp_info = CompanyInfo.objects.all()
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.registered_by = request.user
            obj.save()
            product_name = form.cleaned_data.get('title')
            messages.success(request, f" {product_name} successfully added to your products")
        else:
            messages.error(request, f"Sorry, we could not save the product")
    form = ProductForm()
    arg = {'comp_info': comp_info, 'form': form}
    return render(request, 'main/private/product/add_product.html',  arg)


def products(request):
    comp_info = CompanyInfo.objects.all()
    arg = {'title': 'our products', 'page_name': 'our products', 'products': Product.objects.all(), 'comp_info': comp_info,}
    return render ( request, 'main/public/products.html', arg )

def product_detail(request, slug):
    comp_info = CompanyInfo.objects.all ()
    product = Product.objects.get(slug=slug)
    arg={'product': product, 'comp_info':comp_info}
    return render(request, 'main/public/product_detail.html', arg)


def msg_list(request):
    msg = ContactUs.objects.all().order_by('-id')
    comp_info = CompanyInfo.objects.all()
    paginator = Paginator (msg, 2)
    page_number = request.GET.get('page')
    msg_obj = Paginator.get_page(paginator, page_number)

    arg = {'title': 'Messages list', 'page_name': 'Messages list', 'msg_obj': msg_obj, 'comp_info': comp_info,}
    return render ( request, 'main/private/messages/messages_list.html', arg )

def msg_detail(request, id):
    comp_info = CompanyInfo.objects.all()
    msg = ContactUs.objects.get(id=id)
    arg={'msg': msg, 'comp_info':comp_info}
    return render(request, 'main/private/messages/message_detail.html', arg)


def delete_msg(request, pk):
    obj = ContactUs.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('main:msg_list')
    comp_info = CompanyInfo.objects.all ()
    arg = {'title': 'message deletion', 'page_name': 'Message deletion', "object": obj, 'comp_info': comp_info}
    return render(request, 'main/private/messages/confirm_delete.html', arg)


def product_list(request):
    try:
        comp_info = CompanyInfo.objects.all ()
        data_set = Product.objects.all()
        paginator = Paginator(data_set, 4)
        page_number = request.GET.get('page')
        product_obj=Paginator.get_page(paginator, page_number)
        arg = {
            'title': 'Product Details ',
            'page_name': 'Product Details',
            'comp_info':comp_info,
            'product_obj': product_obj,

        }
        return render(request, 'main/private/product/product_list.html', arg)
    except NameError:
        messages.error("Up... something went wrong...")



def delete_product(request, pk):
    obj = Product.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('main:product_list')
    comp_info = CompanyInfo.objects.all ()
    arg = {'title': 'product deletion', 'page_name': 'product deletion', "object": obj, 'comp_info': comp_info}
    return render(request, 'main/private/product/confirm_delete.html', arg)


def update_product(request, pk):
    product = Product.objects.get(id=pk)
    search = Product.objects.filter(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('title')
            messages.success(request, f'{product_name}  has been updated!')
            return redirect('main:product_list')
        else:
            form = ProductForm()
    arg = {'title': 'Update product', 'page_name': 'Update product details', 'form': form, 'product': search, }

    return render(request, 'main/private/product/update_product.html', arg)


def add_company(request):
    comp_info = CompanyInfo.objects.all ()
    form = CompanyForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid ():
            obj = form.save (commit=False)
            obj.save ()
            messages.success ( request, "Company Info Successfully Saved" )
        else:
            messages.success ( request, "Company Info couldn't be Saved" )
    form = CompanyForm ()
    arg = {'comp_info': comp_info, 'form': form}
    return render ( request, 'main/private/company/add_company.html', arg)



def contact_us(request):
    comp_info = CompanyInfo.objects.all()
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            contact_name = form.cleaned_data.get ( 'name' )
            messages.success(request, f" Dear {contact_name}, our team will get back to you the soonest possible" )
        else:
            messages.error(request, f"Sorry, we could receive your enquiry... Make sure that you entered the info correctlu")
    form = ContactForm()
    arg = {'title': 'contact us', 'page_name': 'contact us', 'comp_info':comp_info, 'form':form }
    return render ( request, 'main/public/contact.html', arg)

def add_about_company(request):
    comp_info = CompanyInfo.objects.all ()
    form = AboutCompanyForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid ():
            obj = form.save ( commit=False )
            obj.save ()
            messages.success ( request, "About Company Detail Successfully Saved" )
        else:
            messages.success ( request, "Data about the company couldn't be Saved" )
    form = AboutCompanyForm ()
    arg = {'comp_info': comp_info, 'form': form}
    return render ( request, 'main/private/about/add_about.html', arg )


def add_sliders(request):
    comp_info = CompanyInfo.objects.all()
    form = SlideForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            slider_name = form.cleaned_data.get('slideBtnText')
            messages.success(request, f" {slider_name} successfully added to your web app")
        else:
            messages.error(request, f"Sorry, we could not save the slider")
    form = SlideForm()
    arg = {'comp_info': comp_info, 'form': form}
    return render(request, 'main/private/slide/add_slide.html',  arg)


def test(request):
    form = TestForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            testing = form.cleaned_data.get('test')
            form = TestForm
            messages.success(request, f'{testing} saved successfully!' )
    return render (request, 'main/test.html', {'form' : form})


def staff_management(request):
    comp_info = CompanyInfo.objects.all()
    form = StaffForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            messages.success(request, f'{first_name} {last_name} has been saved!')
        else:
            messages.error(request, f"sorry, we could not save your dada")
    form = StaffForm()
    arg = {'title': 'Register staff', 'page_name': "Staff Registration",'comp_info': comp_info, 'form': form}
    return render(request, 'main/private/staff/staff_registration.html', arg)


