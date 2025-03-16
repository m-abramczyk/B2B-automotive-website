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


# def build_breadcrumbs(request):
#     breadcrumbs = []

#     # Extract the path from the request
#     path = request.path.strip('/').split('/')
#     print("DEBUG - Path:", path)
    
#     if not path or path == ['']:
#         print("DEBUG - Home page detected. No breadcrumbs.")
#         # No breadcrumbs for home page
#         return {'breadcrumbs': breadcrumbs}

#     # Attempt to resolve breadcrumbs based on the URL structure
#     parent = None
#     for part in path:
#         try:
#             # Try to get the Page
#             page = Page.objects.get(slug=part, parent=parent, is_published=True)
#             breadcrumbs.append({
#                 'title': page.menu_title,
#                 'url': page.get_absolute_url(),
#             })
#             print(f"DEBUG - Added breadcrumb for page: {page.menu_title}")
#             parent = page
#         except Page.DoesNotExist:
#             # Try to get CaseStudy if not a Page
#             if parent and parent.is_case_studies_index:
#                 case_study = CaseStudy.objects.filter(slug=part, is_published=True).first()
#                 if case_study:
#                     breadcrumbs.append({
#                         'title': case_study.menu_title,
#                         'url': case_study.get_absolute_url(),
#                     })
#                     print(f"DEBUG - Added breadcrumb for case study: {case_study.menu_title}")
#             break

#     print("DEBUG - Final breadcrumbs:", breadcrumbs)
#     return {'breadcrumbs': breadcrumbs}

# def build_breadcrumbs(request):
#     breadcrumbs = []

#     # Extract the path and remove empty parts
#     path = [part for part in request.path.strip('/').split('/') if part]
#     print("DEBUG - Raw Path:", path)

#     # Detect and skip the language code (assuming it's always two letters)
#     if path and len(path[0]) == 2:
#         path = path[1:]
#     print("DEBUG - Path after skipping language code:", path)

#     # If the path is now empty, it's the home page
#     if not path:
#         return {'breadcrumbs': breadcrumbs}

#     parent = None
#     for part in path:
#         try:
#             # Attempt to find a published Page with this slug and parent
#             page = Page.objects.get(slug=part, parent=parent, is_published=True)
#             breadcrumbs.append({
#                 'title': page.menu_title,
#                 'url': page.get_absolute_url(),
#             })
#             print(f"DEBUG - Added breadcrumb for page: {page.menu_title}")
#             parent = page
#         except Page.DoesNotExist:
#             # If the parent is a case study index, check for a case study
#             if parent and parent.is_case_studies_index:
#                 case_study = CaseStudy.objects.filter(slug=part, is_published=True).first()
#                 if case_study:
#                     breadcrumbs.append({
#                         'title': case_study.menu_title,
#                         'url': case_study.get_absolute_url(),
#                     })
#                     print(f"DEBUG - Added breadcrumb for case study: {case_study.menu_title}")
#             break

#     print("DEBUG - Final breadcrumbs:", breadcrumbs)
#     return {'breadcrumbs': breadcrumbs}