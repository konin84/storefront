from django.shortcuts import render, redirect, get_list_or_404
from .forms import *
from .models import *
from main.models import CompanyInfo
from django.contrib import messages
# Create your views here.


def gallery(request):
    comp_info = CompanyInfo.objects.all()
    category = request.GET.get('category')
    if category is None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)
    categories = Category.objects.all()
    arg = {
        'categories': categories,
        'photos': photos,
        'title': 'Gallery',
        'page_name': 'Gallery Management',
        'comp_info': comp_info,

    }
    return render(request, 'gallery/gallery.html', arg)


def public_gallery(request):
    comp_info = CompanyInfo.objects.all ()
    category = request.GET.get('category')
    if category is None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)
    categories = Category.objects.all()
    arg = {
        'categories': categories,
        'photos': photos,
        'title': 'Our Gallery',
        'page_name': 'Our Gallery',
        'comp_info': comp_info,
    }
    return render(request, 'gallery/public_gallery.html', arg)


def add(request):
    comp_info = CompanyInfo.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                images=image
            )
        return redirect('gallery:gallery')
    arg = {'title': 'Add photo', 'page_name': 'Add photo', 'categories': categories, 'comp_info': comp_info,}
    return render(request, 'gallery/add.html', arg)


def update_picture(request, pk):
    comp_info = CompanyInfo.objects.all ()
    picture = Photo.objects.get(id=pk)
    search = Photo.objects.filter(id=pk)
    form = PhotoForm(instance=picture)
    try:
        if request.method == 'POST':
            form = PhotoForm(request.POST, request.FILES, instance=picture)
            if form.is_valid():
                form.save()
                messages.success(request, f'Picture details updated successfully!')
                return redirect('gallery:gallery')
            else:
                form = PhotoForm()
        arg = {'title': 'Update picture', 'page_name': "Update picture",
               'form': form, 'picture': search,  'comp_info': comp_info,}
        return render(request, 'gallery/update_photo.html', arg)
    except NameError:
        messages.error("There is an error...")


def delete_photo(request, pk):
    comp_info = CompanyInfo.objects.all()
    obj = Photo.objects.get(id=pk)
    if request.method == "POST":
        # confirming delete object
        obj.delete()
        # after deleting redirect to
        return redirect('gallery:gallery')
    arg = {'title': 'photo deletion', 'page_name': 'photo deletion', "object": obj,
           'comp_info': comp_info,}
    return render(request, 'gallery/delete_photo.html', arg)


def view(request, pk):
    comp_info = CompanyInfo.objects.all()
    photo = Photo.objects.get(id=pk)
    arg = {
        'photo': photo,
        'comp_info': comp_info,
    }
    return render(request, 'gallery/photo.html', arg)
