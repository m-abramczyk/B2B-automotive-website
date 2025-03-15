from django.utils.translation import gettext as _
from django.shortcuts import render, get_object_or_404

from .models import HomePage, Page, PageNotFound


#////////////////////////////////////////////////////
# Home Page

def home_page(request):

    page_data = HomePage.objects.first()
    cover = page_data.cover.first()

    context = {
        'page_data': page_data,
        'cover': cover,
    }

    return render(request, 'index.html', context)


#////////////////////////////////////////////////////
# General Page

def general_page(request, slug):

    slug_parts = slug.strip('/').split('/')
    parent = None
    page = None

    for part in slug_parts:
        page = get_object_or_404(Page, slug=part, parent=parent)
        parent = page  # Update parent for the next iteration

    cover = page.cover.first() if page else None

    context = {
        'page_data': page,
        'cover': cover,
    }

    return render(request, 'page-general.html', context)

#////////////////////////////////////////////////////
# Contact Page

def contact_page(request):

    context = {

    }

    return render(request, 'page-contact.html', context)


#////////////////////////////////////////////////////
# 404 Page

def page_not_found(request, exception):
    
    try:
        page_not_found = PageNotFound.objects.first()
    except PageNotFound.DoesNotExist:
        page_not_found = None

    context = {
        'page_not_found': page_not_found
    }

    return render(request, '404.html', context, status=404)