from django.utils.translation import gettext as _
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import HomePage, Page, Contact, PrivacyPolicy, PageNotFound


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
        parent = page

    # if page.is_case_studies_index:
    #     case_studies = CaseStudy.objects.filter(published=True).order_by('-year')
    # else:
    #     case_studies = []
    cover = page.cover.first() if page else None

    context = {
        'page_data': page,
        'cover': cover,
    }

    return render(request, 'page-general.html', context)


#////////////////////////////////////////////////////
# Contact Page

def contact_page(request):

    contact_page = Contact.objects.first()
    contact_page_links = contact_page.externallink_set.order_by('order')
    contact_page_link_header = contact_page_links.first()

    context = {
        'contact_page': contact_page,
        'contact_page_links': contact_page_links,
        'contact_page_link_header': contact_page_link_header,
    }

    return render(request, 'page-contact.html', context)


#////////////////////////////////////////////////////
# Priacy Policy Page

def privacy_policy(request):
    
    privacy_policy = PrivacyPolicy.objects.first()
    privacy_policy_buttons = privacy_policy.privacypolicybutton_set.order_by('order')

    context = {
        'privacy_policy': privacy_policy,
        'privacy_policy_buttons': privacy_policy_buttons,
    }

    return render(request, 'page-privacy-policy.html', context)


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