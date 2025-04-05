from django.utils.translation import gettext as _
from django.shortcuts import render, get_object_or_404

from django.db.models import Prefetch
from django.contrib.contenttypes.models import ContentType

from django.core.mail import send_mail
from django.http import JsonResponse
from contact_form.forms import ContactForm

from .models import ContentBlock, ContentBlockImage, HomePage, Page, Contact, PrivacyPolicy, PageNotFound
from case_studies.models import CaseStudy
from special_blocks.helpers import get_special_blocks


#////////////////////////////////////////////////////
# Home Page

def home_page(request):

    page_data = HomePage.objects.first()
    cover = page_data.cover
    expert = page_data.expert

    content_blocks = ContentBlock.objects.filter(
        content_type=ContentType.objects.get_for_model(HomePage),
        object_id=page_data.id,
        ).prefetch_related(
            Prefetch('images', queryset=ContentBlockImage.objects.order_by('order'))
        ).order_by('order')
    
    special_blocks = get_special_blocks(page_data)
    
    meta_title = page_data.meta_title if page_data.meta_title else page_data.title.rstrip(":")
    meta_description = page_data.meta_description
    is_published = True

    context = {
        'page_data': page_data,
        'meta_title': meta_title,
        'meta_description': meta_description,
        'is_published': is_published,
        'cover': cover,
        'expert': expert,
        'content_blocks': content_blocks,
        **special_blocks,
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

    meta_title = page.meta_title if page.meta_title else page.title.rstrip(":")
    meta_description = page.meta_description
    is_published = page.is_published

    context = {
        'page_data': page,
        'meta_title': meta_title,
        'meta_description': meta_description,
        'is_published': is_published,
        'case_studies': [],
        'covers': [],
        'cover': None,
        'expert': None,
        'content_blocks': [],
        'current_sort': None,
    }

    if page.is_case_studies_index:

        case_studies = CaseStudy.objects.filter(is_published=True).select_related('cover').order_by('-year')
        context['case_studies'] = case_studies
        context['covers'] = [cs.cover for cs in case_studies if cs.cover and cs.index_cover_slider]        
        context['expert'] = page.expert
        
    else:

        context['cover'] = page.cover
        context['expert'] = page.expert
        
        context['content_blocks'] = ContentBlock.objects.filter(
            content_type=ContentType.objects.get_for_model(Page),
            object_id=page.id,
        ).prefetch_related(
            Prefetch('images', queryset=ContentBlockImage.objects.order_by('order'))
        ).order_by('order')
        
        special_blocks = get_special_blocks(page)
        context.update(special_blocks)
    
    return render(request, 'page-general.html', context)


#////////////////////////////////////////////////////
# Contact Page

def contact_page(request):

    contact_page = Contact.objects.first()

    contact_page_links = contact_page.externallink_set.order_by('order')
    contact_page_link_header = contact_page_links.first()
    expert = contact_page.expert

    meta_title = contact_page.meta_title if contact_page.meta_title else contact_page.title.rstrip(":")
    meta_description = contact_page.meta_description
    is_published = True

    content_blocks = ContentBlock.objects.filter(
        content_type=ContentType.objects.get_for_model(Contact),
        object_id=contact_page.id,
        ).prefetch_related(
            Prefetch('images', queryset=ContentBlockImage.objects.order_by('order'))
        ).order_by('order')
    
    special_blocks = get_special_blocks(contact_page)

    # Contact Form
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)

        # Check honeypot field
        if form.data.get('middle_name'):
            return JsonResponse({'success': False, 'message': _('Bot detected — message not sent.')})
        
        if form.is_valid():
            send_mail(
                subject='New Contact Form Message',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['maciej.abramczyk@gmail.com'],
            )
            form = ContactForm()
            return JsonResponse({'success': True, 'message': _('Thank you! Your message has been sent!')})
        else:
            errors = {field: error.get_json_data() for field, error in form.errors.items()}

            # print("Form Errors:", form.errors)
            # translated_errors = {}
            # for field, errors in form.errors.items():
            #     translated_errors[field] = [_(str(error)) for error in errors]
            # print("Translated Errors:", translated_errors)
            return JsonResponse({'success': False, 'message': _('Please correct the fields above before sending.'), 'errors': errors})


    context = {
        'contact_page': contact_page,
        'meta_title': meta_title,
        'meta_description': meta_description,
        'is_published': is_published,
        'contact_page_links': contact_page_links,
        'contact_page_link_header': contact_page_link_header,
        'expert': expert,
        'content_blocks': content_blocks,
        'form': form,
        **special_blocks,
    }

    return render(request, 'page-contact.html', context)


#////////////////////////////////////////////////////
# Priacy Policy Page

def privacy_policy(request):
    
    privacy_policy = PrivacyPolicy.objects.first()
    privacy_policy_buttons = privacy_policy.privacypolicybutton_set.order_by('order')

    meta_title = privacy_policy.meta_title if privacy_policy.meta_title else privacy_policy.title.rstrip(":")
    meta_description = privacy_policy.meta_description
    is_published = privacy_policy.is_published

    context = {
        'privacy_policy': privacy_policy,
        'privacy_policy_buttons': privacy_policy_buttons,
        'meta_title': meta_title,
        'meta_description': meta_description,
        'is_published': is_published,
    }

    return render(request, 'page-privacy-policy.html', context)


#////////////////////////////////////////////////////
# 404 Page

def page_not_found(request, exception):
    
    try:
        page_not_found = PageNotFound.objects.first()
    except PageNotFound.DoesNotExist:
        page_not_found = None

    is_published = True

    context = {
        'page_not_found': page_not_found,
        'is_published': is_published,
    }

    return render(request, '404.html', context, status=404)