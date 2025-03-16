from .models import Page, Contact, PrivacyPolicy
from case_studies.models import CaseStudy
from django.db.models import Prefetch


def navigation_context(request):
    # Fetch section parents
    section_1_parent = Page.objects.filter(is_section_1_parent=True, is_published=True).only('menu_title', 'footer_title', 'slug').first()
    section_2_parent = Page.objects.filter(is_section_2_parent=True, is_published=True).only('menu_title', 'footer_title', 'slug').first()

    # Fetch child pages for each section
    section_1_children = Page.objects.filter(parent=section_1_parent, is_published=True).only('menu_title', 'footer_title', 'slug', 'thumbnail').order_by('order') if section_1_parent else []
    section_2_children = Page.objects.filter(parent=section_2_parent, is_published=True).only('menu_title', 'footer_title', 'slug', 'thumbnail').order_by('order') if section_1_parent else []

    # Fetch contact page data
    contact_page = Contact.objects.only('menu_title', 'footer_title', 'address_footer').first()
    contact_page_links = contact_page.externallink_set.order_by('order') if contact_page else []

    # Fetch Privacy Policy data
    privacy_policy = PrivacyPolicy.objects.filter(is_published=True).only('menu_title', 'footer_title').first()

    return {
        'section_1_parent': section_1_parent,
        'section_2_parent': section_2_parent,
        'section_1_children': section_1_children,
        'section_2_children': section_2_children,
        'contact_page': contact_page,
        'contact_page_links': contact_page_links,
        'privacy_policy': privacy_policy,
    }


def build_breadcrumbs(request):
    breadcrumbs = []

    # Extract the path and remove empty parts
    path = [part for part in request.path.strip('/').split('/') if part]

    # Detect and skip the language code (assuming it's always two letters)
    if path and len(path[0]) == 2:
        path = path[1:] # Skip the first part

    # If the path is now empty, it's the home page
    if not path:
        return {'breadcrumbs': breadcrumbs}

    parent = None
    for part in path:
        try:
            # Handle Contact Page (slug='contact')
            if part == 'contact':
                contact_page = Contact.objects.first()
                breadcrumbs.append({
                    'title': contact_page.menu_title,
                    'url': contact_page.get_absolute_url(),
                })
                break

            # Handle Privacy Policy Page (hardcoded URL = 'privacy-policy')
            elif part == 'privacy-policy':
                privacy_policy = PrivacyPolicy.objects.filter(is_published=True).first()
                breadcrumbs.append({
                    'title': privacy_policy.menu_title,
                    'url': privacy_policy.get_absolute_url(),
                })
                break

            # Attempt to find a published Page with this slug and parent
            page = Page.objects.get(slug=part, parent=parent, is_published=True)
            breadcrumbs.append({
                'title': page.menu_title,
                'url': page.get_absolute_url(),
            })
            parent = page

        except Page.DoesNotExist:
            # If the parent is a case study index, check for a case study
            if parent and parent.is_case_studies_index:
                case_study = CaseStudy.objects.filter(slug=part, is_published=True).first()
                if case_study:
                    breadcrumbs.append({
                        'title': case_study.menu_title,
                        'url': case_study.get_absolute_url(),
                    })
            break

    return {'breadcrumbs': breadcrumbs}