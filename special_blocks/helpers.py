from django.contrib.contenttypes.models import ContentType
from pages.models import ContentBlock
from .models import Clients, Founders, Specialists, Timeline

def get_special_blocks(page):
    """
    Given any page object (HomePage, Page, or Contact), fetch special block booleans and data.
    Returns a dictionary with keys: has_clients, clients, has_founders, founders, etc.
    """
    # Dynamically determine the content type of the page model (HomePage, Page, or Contact)
    content_type = ContentType.objects.get_for_model(page)
    
    # Fetch all related ContentBlock objects for this specific page
    content_blocks = ContentBlock.objects.filter(
        content_type=content_type,
        object_id=page.id
    )
    
    # Initialize special block data
    special = {
        'has_clients': False,
        'clients': None,
        'has_founders': False,
        'founders': None,
        'has_specialists': False,
        'specialists': None,
        'has_timeline': False,
        'timeline': None,
    }
    
    # Check each block for special flags
    if content_blocks.filter(append_clients=True).exists():
        special['has_clients'] = True
        special['clients'] = Clients.objects.prefetch_related('logos').first()
        
    if content_blocks.filter(append_founders=True).exists():
        special['has_founders'] = True
        special['founders'] = Founders.objects.prefetch_related('founders').first()
        
    if content_blocks.filter(append_team=True).exists():
        special['has_specialists'] = True
        special['specialists'] = Specialists.objects.prefetch_related('specialists').first()
        
    if content_blocks.filter(append_timeline=True).exists():
        special['has_timeline'] = True
        special['timeline'] = Timeline.objects.prefetch_related('images').first()

    return special