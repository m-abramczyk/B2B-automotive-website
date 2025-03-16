from .models import Page, Contact, PrivacyPolicy

def navigation_context(request):
    # Fetch section parents
    section_1_parent = Page.objects.filter(is_section_1_parent=True, is_published=True).first()
    section_2_parent = Page.objects.filter(is_section_2_parent=True, is_published=True).first()

    # Fetch child pages for each section
    section_1_children = Page.objects.filter(parent=section_1_parent, is_published=True).order_by('order')
    section_2_children = Page.objects.filter(parent=section_2_parent, is_published=True).order_by('order')

    # Fetch contact page data
    contact_page = Contact.objects.first()
    contact_page_links = contact_page.externallink_set.order_by('order')

    # Fetch Privacy Policy data
    privacy_policy = PrivacyPolicy.objects.filter(is_published=True).first()

    return {
        'section_1_parent': section_1_parent,
        'section_2_parent': section_2_parent,
        'section_1_children': section_1_children,
        'section_2_children': section_2_children,
        'contact_page': contact_page,
        'contact_page_links': contact_page_links,
        'privacy_policy': privacy_policy,
    }